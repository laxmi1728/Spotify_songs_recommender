# 🎧 Spotify Songs Recommender (Machine Learning Project)

## 📌 Project Overview

This project builds a **Spotify Song Recommendation System** using **Machine Learning (K-Means Clustering)**.
The model groups songs based on their audio features and recommends similar songs from the same cluster.

A **Streamlit web application** is used to allow users to interact with the model by adjusting song audio features and receiving recommended songs.



##  Live Application

You can access the deployed application here:

🔗 https://spotifysongsrecommender-bfmggksruzisij2kzrjcwp.streamlit.app/

---

##  Machine Learning Approach

The recommendation system uses **K-Means Clustering** to group songs with similar audio characteristics.

### Audio Features Used

* Track Popularity
* Danceability
* Energy
* Key
* Loudness
* Mode
* Speechiness
* Acousticness
* Instrumentalness
* Liveness
* Valence
* Tempo
* Duration (ms)

Songs with similar features are grouped into clusters, and recommendations are generated from the same cluster.



##  Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-Learn**
* **Streamlit**
* **GitHub**
* **Streamlit Cloud**



##  Dataset

The dataset contains Spotify song information including audio features and playlist genres.
These features were used to train the clustering model.



## Project Structure

```
spotify_songs_recommender
│
├── application.py           # Streamlit web application
├── spotify_clustered.csv    # Dataset with cluster labels
├── kmeans_model.pkl         # Trained K-Means model
├── scaler.pkl               # Feature scaler
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation




  How to Run Locally

1️⃣ Clone the repository


git clone https://github.com/laxmi1728/spotify_songs_recommender.git


2️⃣ Install dependencies


pip install -r requirements.txt


3️⃣ Run the Streamlit app

streamlit run application.py



Features of the Application

✔ Predicts song cluster based on audio features
✔ Maps clusters to dominant music genres
✔ Recommends similar songs
✔ Interactive sliders to modify audio features
✔ Clean and responsive UI built with Streamlit



  Application Preview

Users can adjust song audio features and receive recommendations from the same cluster.



 Author

Thota Laxmi Prasanna

Machine Learning Project – Spotify Song Recommendation System

  License

This project is created for educational purposes.
