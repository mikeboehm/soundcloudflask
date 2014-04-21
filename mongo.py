#!/usr/bin/python

# import pymongo
from pymongo import MongoClient
from connection_manager import connectionManager
from pprint import pprint
import json
import os
import datetime
from playlist import Playlist

class sc_database(object):
	
	def __init__(self):
		mongo_client = MongoClient('mongodb://localhost:27017/')
		db = mongo_client.soundcloud_test_database
		self.db = db
# 		collection = db.test_collection
		
		connection = connectionManager()
		self.client = connection.client
	
	def me(self):
		# @todo make DB call instead
		me = self.client.get('/me')
		return me
	
	def update_favorites(self):
		me = self.me()
		favorites = self.client.get('/users/' + str(me.id) + '/favorites', limit=5, offset=5)
# 		decoded = json.JSONDecoder(favorites)
# 		pprint(decoded)
# 		likes = []
		for raw_track in favorites:
			track = {
				'id': raw_track.id,
				'title': raw_track.title,
				'user' : raw_track.user['username'],
				'stream_url': raw_track.stream_url,
				'playback_count': raw_track.playback_count,
				'favoritings_count': raw_track.favoritings_count,
				'duration': raw_track.duration,
				'comment_count': raw_track.comment_count,
				'last_updated': datetime.datetime.utcnow()
			}
			
			
			'''
			@todo Store user's likes as an array for that document(record)	
			Eg: 
				user_id
					track1
					track2
					track3
			
			'''
		 	self.db.tracks.update({'id': track['id']}, track, True)					
# 		 	likes.append(track)
	
	def favorites(self):
# 		me = self.me()
# 		favorites = self.client.get('/users/' + str(me.id) + '/favorites', limit=5, offset=5)	
		find = self.db.tracks.find()
		favorites = []
		for track in find:
			favorites.append(track)
# 			pprint(track)
		return favorites

	def favorites_as_playlist(self):
		find = self.db.tracks.find()
		favorites = Playlist()
		for track in find:
			favorites.add_track(track)
# 			pprint(track)
		return favorites
			
	
	def write_stuff(self):
# 		user = self.client.get('/users/318024')
		me = self.client.get('/me')
		print me.id
		print me.username
		
# 		self.client.get('/tracks/' + user_id=user.id, limit=30, embeddable_by='me')
		tracks = self.client.get('/users/' + str(me.id) + '/favorites', limit=5, offset=5)
		
# 		pprint(vars(me))
		
# 		user = self.client.get('/users/318024')
# 		pprint(vars(user))
		
# 		tracks = self.client.get('/users/318024/tracks')
		for track in tracks:
			pprint(vars(track))
		
# 		print vars(me)
# 		followers = self.get_followers()
# 		for user in followers:
# # 			print vars(user)
# 			print json.dumps(vars(user))
# # 			print user.id
# # 			print user.username
	
	def get_followers(self):
		return self.client.get('/me/followings')


# os.system('clear')	
# mongo = sc_database()
# favorites = mongo.favorites()
# for track in favorites:
#  	print track['last_updated']


# # likes = {'user': {'username':'mike'}}
# # print likes['user']['username']
# likes = []
# for raw_track in raw_likes:
# 	track = {
# 		'id': raw_track.id,
# 		'title': raw_track.title,
# 		'user' : raw_track.user['username'],
# 		'stream_url': raw_track.stream_url,
# 		'playback_count': raw_track.playback_count,
# 		'favoritings_count': raw_track.favoritings_count,
# 		'duration': raw_track.duration,
# 		'comment_count': raw_track.comment_count,
# 		"last_updated": datetime.datetime.utcnow()
# 	}
#  	print mongo.db.tracks.update({'id': track['id']}, track, True)
# 	
# 	likes.append(track)

# pprint(likes)
# mongo_tracks = mongo.db.tracks.insert(likes)
# db_tracks = mongo.db.tracks.find()
# print db_tracks.count()
# for track in favorites:
#  	print track['last_updated']
# 	pprint(track)
# pprint(vars(mongo_tracks))

	
	
	
	
	
	