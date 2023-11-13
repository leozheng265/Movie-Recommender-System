# Movie Recommender

## Introduction
Welcome to the Movie Recommender System, a streamlined tool designed to enhance your movie selection experience. Utilizing a rich dataset from The Movie Database (TMDB) and advanced matching algorithms, this application offers personalized movie suggestions with ease and accuracy.

## Features
- Personalized Recommendations: Utilizes user input to provide tailored movie suggestions, ensuring a personalized browsing experience.
- Fuzzy Search Functionality: Even if you're unsure about a movie's exact title, the intelligent search helps you find the right film.
- TMDB Integration: Direct integration with The Movie Database (TMDB) provides up-to-date movie information and high-quality poster images.

## Usage

### Step 1: Download TMDB Dataset
- Source: Kaggle.
- Link: [Kaggle's TMDB Dataset page](https://www.kaggle.com/datasets/juzershakir/tmdb-movies-dataset).

### Step 2: Generate `.pkl` Files
- Run `model.py` to get model files: 
    `python model.py`

### Step 3: Run the Streamlit App
- Navigate to the directory with `app.py` and run `streamlit run app.py`.
- Enter your TMDB API key when prompted. Apply for an API key [here](https://developer.themoviedb.org/reference/intro/getting-started).

### Interacting with the App
- Search for a movie to get recommendations.
- View recommended movies and their posters.
- The app supports fuzzy title matching.

## Technologies Used
- Python: Primary programming language.
- Streamlit: For the web interface creation.
- Pickle: For data serialization and storage.
- Requests: To make API calls to TMDB.
- Pandas: For data processing and analysis.
- TMDB API: Used for fetching real-time movie data and posters.

## API Reference
The Movie Recommender System leverages The Movie Database (TMDB) API for real-time movie poster retrieval. Here's a brief overview of how the API is integrated:

- Usage: Essential for authenticating and accessing TMDB API services.
- Storage: Entered by the user when the application starts and stored securely for the session.