# Movie Recommendation System 🎬

This project builds a **content-based movie recommender** using metadata such as genres, keywords, taglines, cast, and director.

The implementation follows these key steps:

## 📥 Data Loading and Preprocessing
1. Movie data is loaded from a CSV file.
2. Missing values in selected textual features are filled with empty strings.
3. All selected features are combined into a single string per movie.

## 🧠 Feature Extraction
1. TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert textual data into numerical vectors that capture word importance and frequency.

## 📊 Similarity Computation
1. Cosine similarity is calculated between the TF-IDF vectors to determine how similar each movie is to every other movie in the dataset.

## 🎯 Recommendation Logic
1. The user provides a movie title.
2. The system finds the closest match to that title in the dataset using fuzzy string matching (`difflib.get_close_matches`).
3. Based on the cosine similarity score of the matched movie, it ranks and recommends the top 30 most similar movies.

---

This system is efficient for **small to medium-sized datasets** and provides **personalized recommendations based on movie content**, without requiring user interaction history.
