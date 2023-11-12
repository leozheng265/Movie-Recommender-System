import streamlit as st
import pickle
import re 
import requests

# Function to validate API key (placeholder)
def validate_api_key(key):
    if len(key) != 32:
        return False
    return True  # Placeholder return value

def fetch_poster(movie_id, api_key):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        data = requests.get(url)
        if data.status_code == 200:
            data = data.json()
            poster_path = data.get('poster_path')
            if poster_path:
                full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
                return full_path
            else:
                return 'default.png'  # Path to default poster
        else:
            return 'default.png'
    except Exception as e:
        return 'default.png'

def normalize_string(s):
    """Normalize strings by removing non-alphanumeric characters and making lowercase."""
    return re.sub(r'\W+', '', s).lower()

def fuzzy_matching(movie_title, movie_list):
    normalized_input = normalize_string(movie_title)
    for title in movie_list:
        if normalized_input == normalize_string(title):
            return title
    return None  # Return None if no match found

def recommend(movie, api_key):
    matched_title = fuzzy_matching(movie, movies['original_title'].values)
    if matched_title:
        index = movies[movies['original_title'] == matched_title].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
        recommend_movie = []
        recommend_poster = []
        for i in distance[1:6]:
            movies_id=movies.iloc[i[0]].id
            recommend_movie.append(movies.iloc[i[0]].original_title)
            recommend_poster.append(fetch_poster(movies_id, api_key))
        return recommend_movie, recommend_poster
    else:
        return ["Movie not found. Please check the title and try again."], ['N/A']

# Load movies list and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list=movies['original_title'].values

# Initialize session state
if 'api_key_valid' not in st.session_state:
    st.session_state['api_key_valid'] = False

# Main App Layout
st.header("Movie Recommender System")

# API Key Input Dialog
if not st.session_state['api_key_valid']:
    with st.container():
        st.write("Please enter your TMDB API Key to continue.")
        api_key_input = st.text_input("TMDB API Key", type="password")
        if st.button("Submit"):
            if validate_api_key(api_key_input):
                st.session_state['api_key_valid'] = True
                st.session_state['api_key'] = api_key_input  # Store the API key in session state
                st.experimental_rerun()
            else:
                st.error("Invalid API Key. Please try again.")
else:                
    # Use text_input for movie name input
    user_input = st.text_input("Enter a movie name").strip()

    if st.button("Show Recommendations"):
        # Pass the stored API key to the recommend function
        movie_name, movie_poster = recommend(user_input, st.session_state['api_key'])
        if movie_name[0] == "Movie not found. Please check the title and try again.":
            st.error(movie_name[0])
        else:
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(movie_name[0])
                st.image(movie_poster[0])
            with col2:
                st.text(movie_name[1])
                st.image(movie_poster[1])
            with col3:
                st.text(movie_name[2])
                st.image(movie_poster[2])
            with col4:
                st.text(movie_name[3])
                st.image(movie_poster[3])
            with col5:
                st.text(movie_name[4])
                st.image(movie_poster[4])
