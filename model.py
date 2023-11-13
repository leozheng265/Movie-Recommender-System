import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Data Preparation
movie_data = pd.read_csv('tmdb_movies_data.csv')
movie_data = movie_data[['id', 'original_title', 'overview', 'genres']]
movie_data['tag'] = movie_data['overview'] + movie_data['genres']
movie_data = movie_data.drop(columns=['overview', 'genres'])

# Feature Extraction
cv = CountVectorizer(max_features=10866, stop_words='english')
vector = cv.fit_transform(movie_data['tag'].values.astype('U')).toarray()

# Similarity Calculation
similarity = cosine_similarity(vector)

# Model dumping
pickle.dump(movie_data, open('movie_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))