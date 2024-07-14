import streamlit as st
import pickle
import requests

# Load the movie titles
movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), key=lambda x: x[1], reverse=True)[1:6]

    recommended = []
    recommended_poster=[]
    for i in movie_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        print(movie_id)
        recommended.append(movies_df.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))
    return recommended, recommended_poster

#API hit to fetch poster
def fetch_poster(movie_id):

    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=3472b4848de8e123ac0d4c8cced64f8b&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Streamlit UI
st.title('Movie Recommender System')
selected_movie = st.selectbox("Movie Name", movies_list)

if st.button("Recommend"):
    names,poster = recommend(selected_movie)

    col1, col2, col3 ,col4, col5= st.columns(5)

    with col1:
        st.text("names[0")
        st.image("posters[0]")

    with col2:
        st.text("names[1]")
        st.image("posters[1]")

    with col3:
        st.text("names[2]")
        st.image("posters[2]")

    with col4:
        st.text("names[3]")
        st.image("posters[3]")

    with col5:
        st.text("names[4]")
        st.image("posters[4]")


