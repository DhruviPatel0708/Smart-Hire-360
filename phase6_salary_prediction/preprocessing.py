import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):

    categorical_columns = [
        "education",
        "job_role",
        "skills"
    ]

    encoders = {}

    for col in categorical_columns:

        encoder = LabelEncoder()

        df[col] = encoder.fit_transform(df[col].astype(str))

        encoders[col] = encoder

    return df, encoders