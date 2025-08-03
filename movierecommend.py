import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Inject custom CSS for dark mode and fog white text
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #F5F5F5;
    }
    div[data-testid="stText"], div[data-testid="stMarkdownContainer"] {
        color: #F5F5F5 !important;
    }
    .title {
        font-size: 40px;
        color: #F5F5F5;  /* fog white */
        text-align: center;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .subheader {
        font-size: 26px;
        color: #F5F5F5;  /* fog white */
        margin-top: 30px;
    }
    .movie {
        font-size: 20px;
        color: #DCDCDC;  /* light gray */
        padding: 6px;
    }
    .footer {
        margin-top: 50px;
        font-size: 14px;
        text-align: center;
        color: #888888;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.markdown('<div class="title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)

# Dropdown
selected_movie_name = st.selectbox(
    '🎥 Select a movie to get recommendations:',
    movies['title'].values
)

# Button + Output
if st.button('🍿 Get Recommendations'):
    names = recommend(selected_movie_name)

    st.markdown('<div class="subheader">✨ Recommended Movies:</div>', unsafe_allow_html=True)
    for i, name in enumerate(names, 1):
        st.markdown(f'<div class="movie">{i}. {name}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit | Dark Mode Enabled 🌙</div>', unsafe_allow_html=True)
