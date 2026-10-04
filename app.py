from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = pd.read_csv("spotify_clustered.csv")

# --------------------------------------------------
# Load Trained Model
# --------------------------------------------------

with open("kmeans_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# --------------------------------------------------
# Features used during model training
# --------------------------------------------------

FEATURE_COLS = [
    "track_popularity",
    "danceability",
    "energy",
    "key",
    "loudness",
    "mode",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo",
    "duration_ms"
]

# --------------------------------------------------
# Default Values
# --------------------------------------------------

DEFAULTS = {
    "track_popularity": 50,
    "danceability": 0.50,
    "energy": 0.50,
    "key": 5,
    "loudness": -6.0,
    "mode": 1,
    "speechiness": 0.10,
    "acousticness": 0.20,
    "instrumentalness": 0.05,
    "liveness": 0.20,
    "valence": 0.50,
    "tempo": 120.0,
    "duration_ms": 225000
}


# --------------------------------------------------
# Find Dominant Genre for a Cluster
# --------------------------------------------------

def get_dominant_genre(cluster_id):

    cluster_data = df[df["Cluster"] == cluster_id]

    if cluster_data.empty:
        return "Unknown"

    if "playlist_genre" not in cluster_data.columns:
        return "Unknown"

    genre_counts = cluster_data["playlist_genre"].value_counts()

    if genre_counts.empty:
        return "Unknown"

    return genre_counts.index[0]


# --------------------------------------------------
# Home Route
# --------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    values = DEFAULTS.copy()

    prediction_id = None
    genre = None
    recommendations = []
    error = None

    if request.method == "POST":

        try:

            # ------------------------------------------
            # Read input values
            # ------------------------------------------

            for col in FEATURE_COLS:

                values[col] = float(request.form[col])

            # Integer features

            values["track_popularity"] = int(
                values["track_popularity"]
            )

            values["key"] = int(
                values["key"]
            )

            values["mode"] = int(
                values["mode"]
            )

            # ------------------------------------------
            # Create input dataframe
            # ------------------------------------------

            input_df = pd.DataFrame(
                [[values[col] for col in FEATURE_COLS]],
                columns=FEATURE_COLS
            )

            # ------------------------------------------
            # Scale input
            # ------------------------------------------

            input_scaled = scaler.transform(input_df)

            # ------------------------------------------
            # Predict cluster
            # ------------------------------------------

            prediction_id = int(
                model.predict(input_scaled)[0]
            )

            # ------------------------------------------
            # Determine actual dominant genre
            # ------------------------------------------

            genre = get_dominant_genre(prediction_id)

            # ------------------------------------------
            # Get songs from predicted cluster
            # ------------------------------------------

            cluster_songs = df[
                df["Cluster"] == prediction_id
            ].copy()

            # ------------------------------------------
            # Generate recommendations
            # ------------------------------------------

            if not cluster_songs.empty:

                recommendation_columns = [
                    "track_name",
                    "track_artist",
                    "playlist_genre"
                ]

                recommendations = (
                    cluster_songs[
                        recommendation_columns
                    ]
                    .sample(
                        n=min(5, len(cluster_songs)),
                        random_state=None
                    )
                    .to_dict("records")
                )

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


# --------------------------------------------------
# Run Application
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
