#!/usr/bin/python
from flask import Flask, request, render_template, url_for
import datetime
import os
# from player import player
from mongo import sc_database
from pprint import pprint
from track import Track

app = Flask(__name__)

# Instantiate player object
# player = player()

my_track = Track()

@app.route("/", methods=['GET'])
def index():
	raw_data = open('data.txt')
	processed_data = []
	keys = ['title', 'user', 'permalink', 'duration', 'date', 'track_id']
	for line in raw_data:
		processed_data.append(dict(zip(keys, line.split(' | '))))
	tracks = processed_data
	try: # if there's a sort provided
		sort = request.args.get('sort')
		newlist = sorted(processed_data, key=lambda k: k[sort])
		tracks = newlist
	except KeyError:
		pass

 	return render_template('index.html', tracks=tracks, now_playing="Mad track name")
	
@app.route('/favorites/')
def favourites():
	track_list = []
	for file in os.listdir("favourites"):
		if file.endswith('.txt'):
			fav_file = open('favourites/' + file)
			keys = ['user', 'user_id', 'permalink', 'title', 'date', 'track_id', 'duration']
			processed_data = []
			for line in fav_file:
				processed_data.append(dict(zip(keys, line.split(' | '))))
			track_list.append({'user' : file[:-4], 'tracks' : processed_data})
	return render_template('favourites.html', tracks=track_list)

@app.route('/embedcode/', methods=['GET'])
def embedcode():
	track = request.args.get('track')
	embed = client.get('/oembed', url=track)
	return embed.html.encode('utf8')

@app.route('/likes/', methods=['GET'])
def likes():
	from track import Track
	new_track = Track()

	db = sc_database()
	favorites = db.favorites_as_playlist()
	pprint(dir(favorites))
	for track in favorites.tracks:
		print track.title
	return render_template('likes.html', fav=favorites, track_obj=new_track, now_playing="Mad track name2")
# 	return favorites
# 	track = request.args.get('track')
# 	embed = client.get('/oembed', url=track)
	return embed.html.encode('utf8')

@app.route('/vlc/', methods=['GET'])
def vlc():
# 	os.system('clear')
	track_id = request.args.get('track')
	player.play(track_id)
	return stream_url.location

# @app.route('/player/', methods=['GET'])
# def player():
# 	track = player.track()
# 	print track
# 	print 'player'
# 	print jsonify(track)
# 	return 'player'

@app.route('/stop_vlc/')
def stop_vlc():
	player.stop()
	return "stopped"

if __name__ == "__main__":
	app.debug = True
	app.run()
# 	app.run(host='0.0.0.0')
