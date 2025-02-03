🔧 Predictive Maintenance of Industrial Equipment Using Machine Learning

📌 Overview
Predictive maintenance helps industries reduce downtime and prevent failures by analyzing sensor data using Machine Learning (ML). This project implements a Random Forest Classifier to predict equipment failures in real time. The trained model is integrated into a Flask dashboard with an interactive UI for visualization.

📂 Project Structure
📦 Predictive_Maintenance
 ┣ 📂 static
 ┃ ┗ 📂 css
 ┃   ┗ style.css  # Glassy UI Design
 ┣ 📂 templates
 ┃ ┗ dashboard.html  # Flask Dashboard UI
 ┣ app.py  # Flask App
 ┣ main.py  # Model Training & Prediction
 ┣ predictive_maintenance.csv  # Dataset
 ┣ best_random_forest_model.joblib  # Saved Model
 ┣ requirements.txt  # Dependencies
 ┗ README.md  # Project Documentation

 
🛠 Features
✔ Predictive failure detection using ML
✔ Flask-based interactive dashboard
✔ Real-time probability-based classification
✔ Glassy UI with responsive design
✔ Detailed failure analysis through graphs

📊 Dataset Description
Feature Name	Description
Air temperature [K]	Air temperature in Kelvin
Process temperature [K]	Process temperature in Kelvin
Rotational speed [rpm]	Machine's rotational speed in RPM
Torque [Nm]	Torque applied in Newton-meters
Tool wear [min]	Tool usage time in minutes
Product ID	Unique identifier for the product
Type	Machine type
Target	0 → Normal, 1 → Failure
🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/arya1917/Predective-Maintaiance-.git
cd Predective-Maintaiance-
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Train the Model
python main.py
4️⃣ Run the Flask App
python app.py

Access the dashboard at: http://127.0.0.1:5000/

🔗 Technologies Used
Python, Flask (Backend)
Machine Learning (Scikit-Learn)
Pandas, NumPy (Data Processing)
Matplotlib, Seaborn (Visualization)
HTML, CSS (Glassy UI Design)
🤝 Contributors
Arya Subhash Jadhav (Lead Developer & ML Engineer)
Feel free to contribute by raising issues or submitting pull requests! 🚀
📜 License
This project is licensed under the MIT License.
