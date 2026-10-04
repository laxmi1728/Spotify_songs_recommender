# 🎧 Spotify Songs Recommender (Machine Learning Project)

## 📌 Project Overview

This project builds a **Spotify Song Recommendation System** using **Machine Learning (K-Means Clustering)**.

The model groups songs based on their audio features and recommends similar songs from the same cluster.

A **Flask web application** provides an interactive interface where users can adjust Spotify audio features and receive song recommendations.

The application is deployed using **Render**.

---

## 🌐 Live Application

The Flask application is deployed on Render:

🔗 **Live Demo:**  
`YOUR_RENDER_URL`

---

## 🤖 Machine Learning Approach

The recommendation system uses **K-Means Clustering** to group songs with similar audio characteristics.

### 🎵 Audio Features Used

- Track Popularity
- Danceability
- Energy
- Key
- Loudness
- Mode
- Speechiness
- Acousticness
- Instrumentalness
- Liveness
- Valence
- Tempo
- Duration (ms)

The user's input is scaled using the trained scaler and passed to the trained K-Means model.

The model predicts the most suitable cluster, and songs from that cluster are used to generate recommendations.

---

## 🎯 Cluster Categories

The trained model contains **5 clusters**, mapped to their dominant music categories:

| Cluster | Music Category |
|--------:|----------------|
| 0 | Latin Songs |
| 1 | Rock Songs |
| 2 | R&B / Hip-Hop Songs |
| 3 | Rap Songs |
| 4 | EDM Songs |

> Note: K-Means clusters songs based on their audio features. The music category represents the dominant genre observed within each cluster.

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Pandas**
- **NumPy**
- **Scikit-Learn**
- **HTML**
- **CSS**
- **Gunicorn**
- **GitHub**
- **Render**

---

## 📊 Dataset

The dataset contains Spotify song information including audio features and playlist genres.

The following features are used for prediction:

- Track Popularity
- Danceability
- Energy
- Key
- Loudness
- Mode
- Speechiness
- Acousticness
- Instrumentalness
- Liveness
- Valence
- Tempo
- Duration (ms)

The processed dataset also contains the cluster labels generated using the K-Means model.

---

## 📁 Project Structure

```text
spotify_songs_recommender
│
├── app.py                  # Flask web application
├── spotify_clustered.csv   # Dataset with cluster labels
├── kmeans_model.pkl        # Trained K-Means model
├── scaler.pkl              # Feature scaler
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── templates/
│   └── index.html          # Flask HTML template
│
└── static/
    └── style.css           # Application styling

💻 Run Locally
1️⃣ Clone the Repository
git clone https://github.com/laxmi1728/spotify_songs_recommender.git

2️⃣ Navigate to the Project Folder
cd spotify_songs_recommender

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Flask Application
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000

🚀 Deployment on Render
This project is configured to be deployed as a Flask Web Service on Render.
Render Configuration
Create a new Web Service on Render and connect your GitHub repository.
Use the following settings:
Runtime:
Python 3

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app

Render will install the required dependencies and start the Flask application using Gunicorn.
📦 Required Files for Render
Make sure the following files are present in your GitHub repository:
app.py
requirements.txt
spotify_clustered.csv
kmeans_model.pkl
scaler.pkl
templates/index.html
static/style.css

requirements.txt
Your requirements file should contain:
Flask
pandas
numpy
scikit-learn
gunicorn

✨ Features of the Application
✔ Predicts song clusters using K-Means
✔ Uses 13 Spotify audio features
✔ Maps clusters to dominant music categories
✔ Recommends songs from the predicted cluster
✔ Interactive audio feature controls
✔ Uses a trained StandardScaler
✔ Flask-based web application
✔ Responsive web interface
✔ Deployable on Render  
🔄 Application Workflow
User
 │
 ▼
Enter Spotify Audio Features
 │
 ▼
Feature Scaling
 │
 ▼
Trained K-Means Model
 │
 ▼
Cluster Prediction
 │
 ▼
Music Category
 │
 ▼
Find Songs in Predicted Cluster
 │
 ▼
Song Recommendations

🧠 Model Files
kmeans_model.pkl
Contains the trained K-Means clustering model used to predict the cluster for a new song.

scaler.pkl
Contains the trained feature scaler used to transform user input before sending it to the K-Means model.

spotify_clustered.csv
Contains the processed Spotify dataset along with the generated cluster labels.

📷 Application Preview
Users can adjust Spotify audio features through the Flask web interface.
The application predicts the corresponding cluster and displays the associated music category along with recommended songs.

👩‍💻 Author
Thota Laxmi Prasanna
Machine Learning Project – Spotify Song Recommendation System

📜 License
This project is created for educational purposes.
