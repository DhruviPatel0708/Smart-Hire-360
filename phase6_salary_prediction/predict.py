import pickle
import pandas as pd

# Load model
model = pickle.load(
    open("phase6_salary_prediction/salary_model.pkl", "rb")
)

# Load encoders
education_encoder = pickle.load(
    open("phase6_salary_prediction/education_encoder.pkl", "rb")
)

role_encoder = pickle.load(
   open("phase6_salary_prediction/role_encoder.pkl", "rb")
)

def predict_salary(
    experience,
    education,
    role
):

    # Fix text formatting
    education = education.strip().title()
    role = role.strip().title()

    # Encode education
    education_encoded = education_encoder.transform(
        [education]
    )[0]

    # Encode role
    role_encoded = role_encoder.transform(
        [role]
    )[0]

    # Create dataframe
    features = pd.DataFrame(
        [[
            experience,
            education_encoded,
            role_encoded
        ]],
        columns=[
            "experience",
            "education",
            "job_role"
        ]
    )

    # Predict salary
    prediction = model.predict(features)[0]

    return prediction