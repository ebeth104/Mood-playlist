from flask import Flask, render_template, request
from functions import aggregate_top_artists, authenticate_spotif, aggregate_top_tracks, create_playlist, select_tracks, create_playlist
import spotipy.util as util

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'

scope = 'user-library-read user-top-read user-follow-read playlist-modify-public'

username = "YOUR SPOTIFY USERNAME"
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/mood", methods = ["POST"])
def moodtape():
    mood = request.form['mood']
    mood = float(mood)
    value = authenticate_spotif(token)
    top_artists = aggregate_top_artists(value)
    top_tracks = aggregate_top_tracks(value, top_artists)
    selected_tracks = select_tracks(value, top_tracks, mood)
    create_playlist(value, selected_tracks, mood)
    return ("Head over to your spotify account! There's a new playlist waiting for you:)")
    
if __name__ == "__main__":
	app.run(debug=True)
