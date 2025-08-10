import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

# Fetch poster from TMDB API
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('poster_path', '')
        return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=No+Image"

# Recommend similar movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# Load model data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.set_page_config(page_title="MovieMate 🎬", layout="wide")

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎥 Welcome to MovieMate</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Find your next favorite movie in seconds. Pick one you like and get top 5 recommendations!</h4>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar for input
st.sidebar.header("📽️ Choose a Movie")
selected_movie = st.sidebar.selectbox("Select a movie you like:", movies['title'].values)

# Recommendation button
if st.sidebar.button("🎯 Recommend"):
    names, posters = recommend(selected_movie)
    st.markdown(f"<h3 style='text-align: center;'>Top 5 movies recommended for <span style='color:#ff4b4b;'>{selected_movie}</span>:</h3>", unsafe_allow_html=True)
    st.write("")

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_container_width=True)
            st.markdown(f"<div style='text-align: center; font-weight: bold;'>{names[i]}</div>", unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align: center; font-style: italic; color: gray;'>Use the sidebar to choose a movie and get recommendations ✨</p>", unsafe_allow_html=True)
