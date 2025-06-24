# IMPORTING REQUIRED LIBRARIES
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# DATA COLLECTION AND PRE-PROCESSING

# LOADING THE DATA FROM THE CSV FILE TO A PANDAS DATAFRAME
movies_data = pd.read_csv('/content/movies.csv')

# PRINTING THE FIRST 5 ROWS OF THE DATAFRAME
print(movies_data.head())

# PRINTING THE SHAPE OF THE DATAFRAME (ROWS, COLUMNS)
print(movies_data.shape)

# SELECTING THE RELEVANT FEATURES FOR RECOMMENDATION
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
print(selected_features)

# REPLACING THE NULL VALUES WITH EMPTY STRINGS
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# COMBINING ALL THE SELECTED FEATURES INTO A SINGLE STRING
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']
print(combined_features)

# CONVERTING THE TEXT DATA TO FEATURE VECTORS
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
print(feature_vectors)

# COMPUTING COSINE SIMILARITY SCORE BASED ON FEATURE VECTORS
similarity = cosine_similarity(feature_vectors)
print(similarity)
print(similarity.shape)

# GETTING THE MOVIE NAME INPUT FROM THE USER
movie_name = input('Enter your favourite movie name: ')

# CREATING A LIST WITH ALL MOVIE TITLES FROM THE DATASET
list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)

# FINDING THE CLOSEST MATCH FOR THE USER'S INPUT MOVIE
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)

# SELECTING THE CLOSEST MATCH
close_match = find_close_match[0]
print(close_match)

# FINDING THE INDEX OF THE MATCHED MOVIE TITLE
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

# GETTING A LIST OF SIMILAR MOVIES WITH THEIR SIMILARITY SCORES
similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)
print(len(similarity_score))

# SORTING MOVIES BASED ON SIMILARITY SCORES IN DESCENDING ORDER
sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
print(sorted_similar_movies)

# PRINTING THE TOP 30 RECOMMENDED MOVIES
print('Movies suggested for you:\n')
i = 1
for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index == index]['title'].values[0]
    if i < 30:
        print(i, '.', title_from_index)
        i += 1
