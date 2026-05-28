import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =========================================
# RANK CANDIDATES
# =========================================

def rank_candidates(job_description):

    # =========================================
    # LOAD DATASET
    # =========================================

    df = pd.read_csv(
        "../../phase6 candidate ranking system/datasets/synthetic_ai_recruitment_dataset_5000.csv"
    )

    # =========================================
    # FILL NULL VALUES
    # =========================================

    df.fillna("", inplace=True)

    # =========================================
    # KEEP EMPLOYEE ID
    # =========================================

    df["employee_id"] = df["employee_id"].astype(str)

    # =========================================
    # CREATE COMBINED PROFILE
    # =========================================

    df["combined_text"] = (

        df["job_role"].astype(str) + " " +

        df["skills"].astype(str) + " " +

        df["required_skills"].astype(str) + " " +

        df["resume_text"].astype(str) + " " +

        df["job_description"].astype(str)

    )

    # =========================================
    # TF-IDF VECTORIZATION
    # =========================================

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        [job_description] +
        df["combined_text"].tolist()
    )

    # =========================================
    # COSINE SIMILARITY
    # =========================================

    similarity_scores = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    ).flatten()

    # =========================================
    # BASE SCORE
    # =========================================

    df["score"] = similarity_scores * 100

    # =========================================
    # EXPERIENCE BONUS
    # =========================================

    df["score"] = (
        df["score"] +
        (df["experience_years"] * 2)
    )

    # =========================================
    # PERFORMANCE BONUS
    # =========================================

    df["score"] = (
        df["score"] +
        (df["performance_rating"] * 1.5)
    )

    # =========================================
    # JOB SATISFACTION BONUS
    # =========================================

    df["score"] = (
        df["score"] +
        (df["job_satisfaction"] * 1)
    )

    # =========================================
    # ATTRITION PENALTY
    # =========================================

    df.loc[
        df["attrition"] == "Yes",
        "score"
    ] -= 5

    # =========================================
    # SORT BY SCORE
    # =========================================

    df = df.sort_values(
        by="score",
        ascending=False
    )

    # =========================================
    # RESET INDEX
    # =========================================

    df = df.reset_index(drop=True)

    # =========================================
    # CREATE RANK
    # =========================================

    df["rank"] = df.index + 1

    # =========================================
    # TOP 10 CANDIDATES
    # =========================================

    top_candidates = df[[
        "rank",
        "employee_id",
        "job_role",
        "experience_years",
        "performance_rating",
        "location",
        "attrition",
        "score"
    ]].head(10)

    # =========================================
    # ROUND SCORE
    # =========================================

    top_candidates["score"] = (
        top_candidates["score"].round(2)
    )

    return top_candidates