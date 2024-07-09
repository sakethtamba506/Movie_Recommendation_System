import pandas as pd
import streamlit as st
import pickle
import requests
import joblib
import numpy as np




def fetch(movie_id):
    # print('Fetching movie', movie_id)
    movie_id = f'tt{movie_id:07}'
    url = "https://www.omdbapi.com/?i={}&apikey=83260cc3".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    # print(data)
    return data['Poster']


def recommend(movie):
    index = db[db['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommendations = []
    related_posters = []
    for i in distances[1:6]:
        recommendations.append(db.iloc[i[0]].title)
        related_posters.append(fetch(db.iloc[i[0]].id))
    return recommendations, related_posters


db = joblib.load('movie_list.joblib')
similarity = joblib.load('similarity.joblib')

st.title('Movies Recommender System')

option = st.selectbox('Which Movie would you like to recommend?', db['title'].values)

if st.button('Recommend'):
    recommended, posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended[0])
        st.image(posters[0])
    with col2:
        st.text(recommended[1])
        st.image(posters[1])

    with col3:
        st.text(recommended[2])
        st.image(posters[2])
    with col4:
        st.text(recommended[3])
        st.image(posters[3])
    with col5:
        st.text(recommended[4])
        st.image(posters[4])
