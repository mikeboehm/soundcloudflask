#!/usr/bin/python

# import pymongo
from pymongo import MongoClient
from connection_manager import connectionManager
from pprint import pprint
import json

class sc_database(object):
	
	def __init__(self):
		mongo_client = MongoClient('mongodb://localhost:27017/')
		db = mongo_client.test_database
		self.db = db
		collection = db.test_collection
		
		connection = connectionManager()
		self.client = connection.client

	def write_stuff(self):
		user = self.client.get('/users/318024')
		print vars(user)
# 		followers = self.get_followers()
# 		for user in followers:
# # 			print vars(user)
# 			print json.dumps(vars(user))
# # 			print user.id
# # 			print user.username
	
	def get_followers(self):
		return self.client.get('/me/followings')
	
mongo = sc_database()
mongo.write_stuff()