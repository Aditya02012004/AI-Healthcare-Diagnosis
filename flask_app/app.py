from flask import Flask, render_template, request
import pandas as pd
from datetime import datetime
from scripts.recommendation_logic import combined_recommendation  # Import your recommendation logic

app = Flask(__name__)

# Load your final dataframes, if needed
admissions_df = pd.read_csv('../datasets/mimic-iii-clinical-database-demo-1.4/final_files/final_admissions.csv')
patients_df = pd.read_csv('../datasets/mimic-iii-clinical-database-demo-1.4/final_files/final_patients.csv')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        age = request.form['age']
        gender = request.form['gender']
        problem = request.form['problem']

        blood_group = request.form.get('blood_group')
        blood_pressure = request.form.get('blood_pressure')
        pulse = request.form.get('pulse')
        weight = request.form.get('weight')
        prescription_file = request.files.get('prescription')
        blood_report_file = request.files.get('blood_report')
        xray_report_file = request.files.get('xray_report')

        # Call your recommendation logic here
        recommendation = combined_recommendation(problem, blood_group, blood_pressure, pulse, weight)

        return render_template('result.html', name=name, recommendation=recommendation)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)