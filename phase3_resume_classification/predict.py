import os
import joblib

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
    os.path.join(BASE_DIR, "resume_classifier_model.pkl")
)

vectorizer = joblib.load(
    os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")
)

# ==========================================
# PREDICT FUNCTION
# ==========================================

def predict_role(resume_text):

    text_vector = vectorizer.transform(
        [resume_text]
    )

    prediction = model.predict(
        text_vector
    )

    return prediction[0]