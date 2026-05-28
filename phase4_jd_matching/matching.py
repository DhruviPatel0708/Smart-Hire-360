from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================
# CALCULATE MATCH SCORE
# ==========================================

def calculate_match_score(
        resume_text,
        jd_text
):

    # LOWERCASE

    resume_text = resume_text.lower()

    jd_text = jd_text.lower()

    # ==========================================
    # TF-IDF SIMILARITY
    # ==========================================

    documents = [

        resume_text,
        jd_text

    ]

    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(
        documents
    )

    cosine_score = cosine_similarity(

        tfidf_matrix[0:1],
        tfidf_matrix[1:2]

    )[0][0]

    cosine_score = cosine_score * 100

    # ==========================================
    # SKILL MATCHING
    # ==========================================

    resume_words = set(
        resume_text.split()
    )

    jd_words = set(
        jd_text.split()
    )

    matched_words = resume_words.intersection(
        jd_words
    )

    skill_score = (

        len(matched_words)
        / len(jd_words)

    ) * 100

    # ==========================================
    # FINAL HYBRID SCORE
    # ==========================================

    final_score = (

        cosine_score * 0.4
        +
        skill_score * 0.6

    )

    # ==========================================
    # BONUS LOGIC
    # ==========================================

    if final_score >= 50:

        final_score += 25

    elif final_score >= 30:

        final_score += 15

    elif final_score >= 15:

        final_score += 8

    else:

        final_score += 5

    # LIMIT SCORE

    if final_score > 100:

        final_score = 100

    final_score = round(
        final_score,
        2
    )

    return final_score