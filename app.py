import streamlit as st 
import pickle
import pandas as pd
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list= movies['title'].values


def Recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recomended_movies = []
    for i in movies_list:
        recomended_movies.append(movies.iloc[i[0]].title)
    return recomended_movies


st.title("Movies Recommender System")

selected_movie_name = st.selectbox(
    'how you like ',
    movies['title'].values
)
if st.button('Recommend'):
    Recommendations = Recommend(selected_movie_name)
    for i in Recommendations:
        st.write(i)


st.markdown("<h1 style='text-align: center; color: white; font-size: 25px;'>Hope The Recommendation Saves Your Time</h1>", unsafe_allow_html=True)
