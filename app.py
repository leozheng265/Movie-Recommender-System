import streamlit as st
import streamlit.components.v1 as components
import pickle
import requests

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['original_title'].values

st.header("Leo's Movie Recommender System")
selectvalue=st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index = movies[movies['original_title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie = []
    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]].original_title)
    return recommend_movie

if st.button("Show Recommendations"):
    movie_name = recommend(selectvalue)
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
