from flask import Flask, render_template, request
from getmood import detect_mood
from getsongs import get_mood_tracks
import os

app = Flask(__name__)

# Environment variables (for Spotify API)
app.config['SPOTIPY_CLIENT_ID'] = os.getenv("SPOTIFY_CLIENTID")
app.config['SPOTIPY_CLIENT_SECRET'] = os.getenv("CLIENT_SEC")
app.config['SPOTIPY_REDIRECT_URI'] = os.getenv("REDIRECT_URI")

UPLOAD_FOLDER = "./static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/songs", methods=["POST"])
def songs():
    name = request.form.get("name")
    image = request.files.get("image")

    if not image or image.filename == "":
        return "No image uploaded. Please select an image.", 400

    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    try:
        image.save(image_path)
    except Exception as e:
        return f"Error saving image: {str(e)}", 400

    try:
        mood = detect_mood(image_path)
        songs = get_mood_tracks(mood)
    except Exception as e:
        return f"Error processing image: {str(e)}", 500

    return render_template('result.html', name=name, mood=mood, songs=songs)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
