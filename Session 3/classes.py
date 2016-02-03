class Vector(object):

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = x

	def __getitem__(self, value):
		if value == 0:
			return self.x


vector = Vector(x=1, y=2, z=1)

array = [1, 2, 3]
array[0]

vector[0]
