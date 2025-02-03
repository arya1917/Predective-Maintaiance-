import time
import pandas as pd
from flask import Flask, render_template, jsonify
import joblib
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

model = joblib.load('best_random_forest_model.joblib')
data = pd.read_csv('predictive_maintenance.csv')

le_product = LabelEncoder()
le_type = LabelEncoder()
data['Product ID_enc'] = le_product.fit_transform(data['Product ID'])
data['Type_enc'] = le_type.fit_transform(data['Type'])

feature_cols = [
    'Air temperature [K]',
    'Process temperature [K]',
    'Rotational speed [rpm]',
    'Torque [Nm]',
    'Tool wear [min]',
    'Product ID_enc',
    'Type_enc'
]

data.reset_index(drop=True, inplace=True)
split_index = int(0.8 * len(data))
test_data = data.iloc[split_index:].reset_index(drop=True)
current_index = 0

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/get_prediction')
def get_prediction():
    global current_index, test_data
    if current_index < min(len(test_data), 20):  
        row = test_data.iloc[current_index]
        current_index += 1
        features = row[feature_cols].values.reshape(1, -1)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0].tolist()
        result = {
            'sample': current_index,
            'prediction': 'Failure' if prediction == 1 else 'Normal',
            'probability': probability,
            'true_label': int(row['Target'])
        }
        time.sleep(0.5)
    else:
        result = {'message': 'No more predictions'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
