import streamlit as st
import pickle
import re  # Regular expression library for text manipulation

# Load movies list and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.header("Leo's Movie Recommender System")

# Use text_input for movie name input
user_input = st.text_input("Enter a movie name").strip()

def normalize_string(s):
    """Normalize strings by removing non-alphanumeric characters and making lowercase."""
    return re.sub(r'\W+', '', s).lower()

def fuzzy_matching(movie_title, movie_list):
    normalized_input = normalize_string(movie_title)
    for title in movie_list:
        if normalized_input == normalize_string(title):
            return title
    return None  # Return None if no match found

def recommend(movie):
    matched_title = fuzzy_matching(movie, movies['original_title'].values)
    if matched_title:
        index = movies[movies['original_title'] == matched_title].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
        recommend_movie = []
        for i in distance[1:6]:
            recommend_movie.append(movies.iloc[i[0]].original_title)
        return recommend_movie
    else:
        return ["Movie not found. Please check the title and try again."]

if st.button("Show Recommendations"):
    movie_name = recommend(user_input)
    if movie_name[0] == "Movie not found. Please check the title and try again.":
        st.error(movie_name[0])
    else:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(movie_name[0])
        with col2:
            st.text(movie_name[1])
        with col3:
            st.text(movie_name[2])
        with col4:
            st.text(movie_name[3])
        with col5:
            st.text(movie_name[4])
