# MovieTVRecs

- EnglishMoviesRecs.ipynb:
  - This project is a movie recommendation system implemented in Python using Flask.
  - It uses a dataset of movies with features like overview, genres, vote average, and popularity.
  - The TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer from scikit-learn is used to convert text data into numerical form.
  - Nearest Neighbors algorithm is used to find movies similar to a given movie based on their TF-IDF vector representations.
  - The Flask web framework is used to create a simple web application where users can input a movie name and get a list of recommended movies.
  - The recommendations are based on the movie's overview, genres, vote average, and popularity.


- MovieRecsGenre.ipynb:
  - Data Loading: The project loads movie datasets for different genres from CSV files. It checks if the 'description' column exists in the dataset (except for the 'telugu' genre, which uses 'Overview' instead), and creates a new column 'features' that combines relevant columns like description, rating, director, and votes into a single text string.
  - TF-IDF Vectorization: For each genre, a TF-IDF vectorizer is created to convert the 'features' column into a TF-IDF matrix, which represents the importance of each word in the 'features' text relative to the entire dataset.
  - Nearest Neighbors Model: A k-nearest neighbors model is trained for each genre using the TF-IDF matrix. This model finds the k most similar movies to a given movie based on their TF-IDF representations.
  - Recommendation Function: The get_recommendations_with_overviews function takes a movie name, genre, and the pre-trained models and data as inputs. It retrieves the TF-IDF matrix and nearest neighbors model for the specified genre. It then finds the TF-IDF representation of the input movie, identifies the k nearest neighbors, and returns a list of recommended movies along with their overviews.
  - Usage: To use this system, you would call the get_recommendations_with_overviews function with a movie name and genre to get a list of recommended movies for that genre based on the input movie's features.

 
- TvRecs.ipynb:
  - 
