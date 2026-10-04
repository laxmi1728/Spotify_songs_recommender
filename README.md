# Spotify Songs Recommender — Flask

Flask version of the Spotify K-Means clustering application.

## Required project files

```text
spotify_flask_project/
├── app.py
├── spotify_clustered.csv
├── kmeans_model.pkl
├── scaler.pkl
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

Put your existing `spotify_clustered.csv`, `kmeans_model.pkl`, and `scaler.pkl` in the project root.

## Run

```bash
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

The 13 features and their order must match the model training:
track_popularity, danceability, energy, key, loudness, mode,
speechiness, acousticness, instrumentalness, liveness, valence,
tempo, duration_ms.
