import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load and preprocess data for each genre
genres = ['action', 'adventure', 'animation', 'biography', 'crime', 'dataset', 'family', 'fantasy', 'history', 'horror', 'mystery', 'romance', 'scifi', 'sports', 'thriller', 'war']  # Add more genres as needed
genre_data = {}
for genre in genres:
    genre_data[genre] = pd.read_csv(f'{genre}_dataset.csv')
    genre_data[genre]['features'] = genre_data[genre]['description'] + ' ' + genre_data[genre]['director']

# TF-IDF Vectorization for each genre
tfidf_models = {}
for genre in genres:
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(genre_data[genre]['features'])
    tfidf_models[genre] = (tfidf, tfidf_matrix)

# Fit Nearest Neighbors models for each genre
nn_models = {}
for genre in genres:
    nn_model = NearestNeighbors(n_neighbors=6, algorithm='auto')
    nn_model.fit(tfidf_models[genre][1])
    nn_models[genre] = nn_model

# Function to get recommendations
def get_recommendations(movie_name, genre, tfidf_models=tfidf_models, nn_models=nn_models):
    tfidf, tfidf_matrix = tfidf_models[genre]
    nn_model = nn_models[genre]

    # Transform input movie into TF-IDF vector
    movie_features = genre_data[genre][genre_data[genre]['movie_name'] == movie_name]['features'].iloc[0]
    movie_tfidf = tfidf.transform([movie_features])

    # Find nearest neighbors
    distances, indices = nn_model.kneighbors(movie_tfidf)

    # Get the movie indices (excluding the input movie)
    movie_indices = indices.flatten()[1:]

    # Return the top 5 recommended movie names
    return genre_data[genre]['movie_name'].iloc[movie_indices].tolist()

# Example usage
genre = 'Action'
movie_name = 'Avengers: Infinity War'
recommendations = get_recommendations(movie_name, genre)
print(recommendations)
