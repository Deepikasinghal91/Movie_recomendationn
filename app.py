import streamlit as st
import pickle
movies_list=pickle.load(open('movies.pkl','rb'))
movies_list=movies_list['title'].values
st.title('Movie Recommender System')
option =st.selectbox(
movies_list
)