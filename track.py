class Track(object):
	def __init__(self, track = False):
		if(track):
			self.title = track['title']
			self.user = track['user']
		else:	
			self.title = 'my track'
			self.artist = 'Mikey B and the Funky Bunch'
	
	def test(self):
		print '=' * 50
		print 'Track Tested!'
		print '=' * 50
		
	def get_track(self, id) :
		pass
		
	def save_track(self):
		pass