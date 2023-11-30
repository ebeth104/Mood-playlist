from flask import Flask, render_template, request
from functions import aggregate_top_artists, authenticate_spotif, aggregate_top_tracks, create_playlist, select_tracks, create_playlist
import spotipy.util as util

client_id = '6c1e24b937c248c59e6d4754603372f0'
client_secret = '6f9833cbad264c49be921ca7be7cf90c'
redirect_uri = 'http://localhost:5000'

scope = 'user-library-read user-top-read user-follow-read playlist-modify-public'

username = "lily"
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