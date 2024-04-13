# MovieTVRecs

- MovieRecsGenre.ipynb:
  - Data Loading: The project loads movie datasets for different genres from CSV files. It checks if the 'description' column exists in the dataset (except for the 'telugu' genre, which uses 'Overview' instead), and creates a new column 'features' that combines relevant columns like description, rating, director, and votes into a single text string.
  - TF-IDF Vectorization: For each genre, a TF-IDF vectorizer is created to convert the 'features' column into a TF-IDF matrix, which represents the importance of each word in the 'features' text relative to the entire dataset.
  - Nearest Neighbors Model: A k-nearest neighbors model is trained for each genre using the TF-IDF matrix. This model finds the k most similar movies to a given movie based on their TF-IDF representations.
  - Recommendation Function: The get_recommendations_with_overviews function takes a movie name, genre, and the pre-trained models and data as inputs. It retrieves the TF-IDF matrix and nearest neighbors model for the specified genre. It then finds the TF-IDF representation of the input movie, identifies the k nearest neighbors, and returns a list of recommended movies along with their overviews.
  - Usage: To use this system, you would call the get_recommendations_with_overviews function with a movie name and genre to get a list of recommended movies for that genre based on the input movie's features.

 
- TvRecs.ipynb:
  - Data Processing: It starts by loading a CSV file (tvshows.csv) containing TV show data into a pandas DataFrame. It then creates a new column called 'features' that combines several columns (overview, vote_average, popularity, original_language) into a single string that represents the features of each TV show.
  - TF-IDF Vectorization: It uses TfidfVectorizer from scikit-learn to convert the 'features' column into a TF-IDF matrix, which represents the importance of each word in the 'features' text relative to the entire dataset.
  - Nearest Neighbors Model: It uses NearestNeighbors from scikit-learn to build a model that can find the nearest neighbors (similar TV shows) for a given TV show based on its TF-IDF representation. The model is fitted on the TF-IDF matrix.
  - Recommendation Function: The get_recommendations_with_overviews function takes a TV show name as input, finds the TF-IDF representation of the input show, and then uses the nearest neighbors model to find similar TV shows. It returns a list of recommended TV show names.
  - Flask Web Application: The project uses Flask to create a web application with two routes:
    - The '/' route renders an index.html template, which is the homepage.
    - The '/recommendations' route accepts a POST request with a form submission containing a movie name.
    - It then calls the get_recommendations_with_overviews function to get recommendations for that movie and renders a 'recommendations.html' template with the recommendations

- EnglishMovieRecs.ipynb:
  - Data Loading and Preprocessing: You load a CSV file (english.csv) containing movie data into a Pandas DataFrame (combined_data). You then create a new column features that combines several columns (overview, genres, vote_average, popularity) into a single feature string for each movie.
  - Feature Extraction: You use TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to convert the textual features into a numerical format (tfidf_matrix) that can be used by machine learning models.
  - Nearest Neighbors Model: You create a NearestNeighbors model (nn_model) to find similar movies based on their TF-IDF vectors. The model is fitted with the TF-IDF matrix.
  - Recommendation Function: The get_recommendations_with_overviews function takes a movie name as input, retrieves its TF-IDF vector, and finds the nearest neighbors (similar movies) using the NearestNeighbors model. It returns a list of recommended movie titles.
  - Flask Web Application: You create a Flask web application with two routes. The index route ('/') renders an HTML template (index.html) for the user to input a movie name. The /recommendations route processes the form submission, calls the get_recommendations_with_overviews function, and renders a template (recommendations.html) with the recommended movies.
