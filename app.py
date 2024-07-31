import streamlit as st
import pickle
import pandas as pd

movie_dict = pickle.load(open("movie_dict.pkl", 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open("similar.pkl", 'rb'))

def recommend(movie):
    movie_index = movies[movies['title']==movie].index [0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommend_movies=[]
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)

    return recommend_movies

st.title("Movie Recommender System")
selected_movie_name = st.selectbox("Search your movies...", movies['title'].values)

if st.button("RECOMMEND"):
    rec = recommend(selected_movie_name)
    for i in rec:
        st.write(i)