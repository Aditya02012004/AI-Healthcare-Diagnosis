def combined_recommendation(problem, blood_group=None, blood_pressure=None, pulse=None, weight=None):
    recommendations = []

    # Basic recommendation based on problem description
    if "pneumonia" in problem.lower():
        recommendations.append("Pneumonia detected. Recommended medicine: Azithromycin.")
    elif "sepsis" in problem.lower():
        recommendations.append("Sepsis detected. Recommended medicine: Ceftriaxone, Vancomycin.")
    elif "diabetes" in problem.lower():
        recommendations.append("Diabetes detected. Recommended medicine: Metformin.")
    elif "hypertension" in problem.lower():
        recommendations.append("Hypertension detected. Recommended medicine: Lisinopril.")
    elif "asthma" in problem.lower():
        recommendations.append("Asthma detected. Recommended medicine: Albuterol.")
    else:
        recommendations.append("Consult a physician for further evaluation.")

    # Additional recommendations based on user inputs
    if blood_group:
        recommendations.append(f"Blood group: {blood_group}.")

    if blood_pressure:
        recommendations.append(f"Blood pressure: {blood_pressure}.")

    if pulse:
        recommendations.append(f"Current pulse: {pulse}.")

    if weight:
        recommendations.append(f"Current weight: {weight}.")

    # Custom advice based on collected data
    if blood_pressure and int(blood_pressure.split('/')[0]) > 140:
        recommendations.append("Consider a low-sodium diet and regular exercise.")

    if pulse and int(pulse) > 100:
        recommendations.append("Consider relaxation techniques and consult a doctor.")

    return " ".join(recommendations) if recommendations else "Consult a physician for further evaluation."
