from track import Track
class Playlist(object):
	def __init__(self):
		self.tracks = []
	
	def current_track(self):
		pass
	
	def next_track(self):
		pass
		
	def previous_track(self):
		pass
	
	def add_track(self, track):
		new_track = Track(track)
		self.tracks.append(new_track)
		print self.tracks
		
	def tracks(self):
		return self.tracks