import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -----------------------------
# Load Dataset and Model
# -----------------------------

df = pd.read_csv("spotify_clustered.csv")

model = pickle.load(open("kmeans_model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(page_title="Spotify songs Recommender", layout="wide")

# -----------------------------
# Custom CSS Styling
# -----------------------------

st.markdown("""
<style>

body {
background: linear-gradient(135deg,#0f172a,#020617);
}

.main-title{
text-align:center;
font-size:45px;
font-weight:700;
color:#1DB954;
}

.subtitle{
text-align:center;
font-size:18px;
color:#cbd5f5;
margin-bottom:30px;
}

.song-card{
background:#1e293b;
padding:15px;
border-radius:12px;
margin-bottom:15px;
box-shadow:0 4px 10px rgba(0,0,0,0.4);
}

.song-title{
font-size:20px;
font-weight:bold;
color:white;
}

.song-artist{
color:#94a3b8;
}

.result-box{
background:#1DB954;
padding:20px;
border-radius:12px;
text-align:center;
font-size:24px;
font-weight:bold;
color:white;
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title Section
# -----------------------------

st.markdown('<div class="main-title">🎧 Spotify songs Recommender</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Machine Learning based Music Clustering System</div>', unsafe_allow_html=True)

# -----------------------------
# Sidebar Inputs
# -----------------------------

st.subheader("Song Audio Features")

col1, col2, col3 = st.columns(3)

with col1:
    track_popularity = st.slider("Track Popularity",0,100,50)
    danceability = st.slider("Danceability",0.0,1.0,0.5)
    energy = st.slider("Energy",0.0,1.0,0.5)
    key = st.slider("Key",0,11,5)

with col2:
    loudness = st.slider("Loudness",-60.0,0.0,-5.0)
    mode = st.slider("Mode",0,1,1)
    speechiness = st.slider("Speechiness",0.0,1.0,0.1)
    acousticness = st.slider("Acousticness",0.0,1.0,0.5)

with col3:
    instrumentalness = st.slider("Instrumentalness",0.0,1.0,0.0)
    liveness = st.slider("Liveness",0.0,1.0,0.1)
    valence = st.slider("Valence",0.0,1.0,0.5)
    tempo = st.slider("Tempo",50.0,200.0,120.0)
    duration_ms = st.slider("Duration (ms)",100000,400000,200000)


# -----------------------------
# Prepare Feature Array
# -----------------------------
# ... (imports and CSS remain the same) ...

# -----------------------------
# Prepare Feature Array
# -----------------------------
# Ensure this list matches EXACTLY the columns you used in your Colab training
feature_cols = ['track_popularity', 'danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'duration_ms']

# Create the input array with ALL features used during training
# -----------------------------
# Prepare Feature Array (FIXED: Added missing features)
# -----------------------------

# The order must match exactly what you did in Google Colab
# Based on your error, we need to include all 13 features
input_data = np.array([[
    track_popularity,
    danceability,
    energy,
    key,
    loudness,
    mode,
    speechiness,
    acousticness,
    instrumentalness,
    liveness,
    valence,
    tempo,
    duration_ms
]])

# -----------------------------
# Predict Cluster
# -----------------------------

predict = st.button("Predict Genre & Recommend Songs")

if predict:
        # 1. Scale the input using the 13 features
        input_scaled = scaler.transform(input_data)
        
        # 2. Get the prediction
        prediction_id = model.predict(input_scaled)[0]

        st.write("Predicted Cluster:", prediction_id)

        # 3. Professional Genre Mapping
        # Note: Check your Colab to ensure these names align with your clusters
        cluster_names = {
            0: "Latin Songs",
            1: "Rock Songs",
            2: "R&B / Hip-Hop Songs",
            3: "Rap Songs",
            4: "EDM Songs"
        }

        genre = cluster_names.get(prediction_id,"Unknown")

        st.markdown(f"""
        <div class="result-box">
        Predicted Genre: {genre}
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------
    # Song Recommendations
    # -----------------------------

        st.subheader("Recommended Songs")

        cluster_songs = df[df['Cluster'] == prediction_id]

        recommendations = cluster_songs[['track_name','track_artist','playlist_genre']].sample(
            min(5, len(cluster_songs))
        )

        for index,row in recommendations.iterrows():

            st.markdown(f"""
            <div class="song-card">

            <div class="song-title">🎵 {row['track_name']}</div>

            <div class="song-artist">
            Artist: {row['track_artist']} <br>
            Genre: {row['playlist_genre']}
            </div>

            </div>
            """, unsafe_allow_html=True)