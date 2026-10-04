from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

df = pd.read_csv("spotify_clustered.csv")

with open("kmeans_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

FEATURE_COLS = [
    "track_popularity", "danceability", "energy", "key", "loudness",
    "mode", "speechiness", "acousticness", "instrumentalness",
    "liveness", "valence", "tempo", "duration_ms"
]

CLUSTER_NAMES = {
    0: "Latin Songs",
    1: "Rock Songs",
    2: "R&B / Hip-Hop Songs",
    3: "Rap Songs",
    4: "EDM Songs"
}

DEFAULTS = {
    "track_popularity": 50, "danceability": 0.50, "energy": 0.50,
    "key": 5, "loudness": -5.0, "mode": 1, "speechiness": 0.10,
    "acousticness": 0.50, "instrumentalness": 0.00, "liveness": 0.10,
    "valence": 0.50, "tempo": 120.0, "duration_ms": 200000
}

@app.route("/", methods=["GET", "POST"])
def home():
    values = DEFAULTS.copy()
    prediction_id = None
    genre = None
    recommendations = []
    error = None

    if request.method == "POST":
        try:
            for col in FEATURE_COLS:
                values[col] = float(request.form[col])

            values["track_popularity"] = int(values["track_popularity"])
            values["key"] = int(values["key"])
            values["mode"] = int(values["mode"])

            input_data = np.array([[
                values["track_popularity"], values["danceability"],
                values["energy"], values["key"], values["loudness"],
                values["mode"], values["speechiness"], values["acousticness"],
                values["instrumentalness"], values["liveness"], values["valence"],
                values["tempo"], values["duration_ms"]
            ]])

            input_scaled = scaler.transform(input_data)
            prediction_id = int(model.predict(input_scaled)[0])
            genre = CLUSTER_NAMES.get(prediction_id, "Unknown")

            cluster_songs = df[df["Cluster"] == prediction_id]
            if len(cluster_songs) > 0:
                recommendations = cluster_songs[
                    ["track_name", "track_artist", "playlist_genre"]
                ].sample(n=min(5, len(cluster_songs))).to_dict("records")

        except Exception as e:
            error = f"Prediction error: {e}"

    return render_template(
        "index.html",
        values=values,
        prediction_id=prediction_id,
        genre=genre,
        recommendations=recommendations,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
