import os
import joblib
import pandas as pd

# ==========================================
# BASE DIRECTORY
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load(
    os.path.join(BASE_DIR, "retention_model.pkl")
)

label_encoders = joblib.load(
    os.path.join(BASE_DIR, "label_encoders.pkl")
)

# ==========================================
# PREDICTION FUNCTION
# ==========================================

def predict_retention(

        experience,
        salary,
        overtime,
        job_satisfaction,
        years_since_promotion,
        work_life_balance

):

    # ======================================
    # LOGIC BASED PREDICTION
    # ======================================

    score = 0

    # EXPERIENCE

    if experience >= 5:
        score += 25
    else:
        score += 10

    # SALARY

    if salary >= 60000:
        score += 25
    else:
        score += 10

    # OVERTIME

    if overtime == "No":
        score += 20
    else:
        score += 5

    # JOB SATISFACTION

    score += (job_satisfaction * 10)

    # WORK LIFE BALANCE

    score += (work_life_balance * 5)

    # YEARS SINCE PROMOTION

    if years_since_promotion <= 2:
        score += 15
    else:
        score += 5

    # ======================================
    # FINAL RESULT
    # ======================================

    if score >= 80:

        return "Employee Likely To Stay"

    else:

        return "Employee Likely To Leave"