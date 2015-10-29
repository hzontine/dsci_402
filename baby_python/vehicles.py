import math

class Vehicle:
	def __init__(self, vid, capacity, location = (0,0), direction = (0,0), owner = None): #constructor
		self.vid = vid
		self.capacity = capacity
		self.location = location
		self.direction = direction
		self.owner = owner
	def print_info(self):
		print ("Vehicle ID: " + str(self.vid))
		print ("Capacity: " + str(self.capacity))
		print ("Location: " + str(self.location))
		print ("Direction: " + str(self.direction))
		print ("Owner: " + str(self.owner))
	def set_direction(self, dx, dy):
		self.direction = (dx, dy)
	def base_move(self, distance):
		dx, dy = self.direction
		scale = distance / math.sqrt((dx ** 2) + (dy ** 2))
		x, y = self.location
		self.location = (x + (scale * dx), y + (scale * dy))
		return self.location
	
	
class Car(Vehicle):
	def __init__(self, vid, capacity, location = (0,0), direction = (0,0), owner = None, 
				fuel_capacity = 15, mpg = 30.0, fuel_level = 10.0):
		#------------------------------------------------------
		#vehicle(self).__init__(vid, capacity, location, direction, owner = None)
		#Mini homework to figure out how to do this the right way
		#Google it!
		#------------------------------------------------------
		#This is the wrong way:
		self.vid = vid
		self.capacity = capacity
		self.location = location
		self.direction = direction
		self.owner = owner
		#------------------------------------------------------
		self.fuel_capacity = fuel_capacity
		self.mpg = mpg
		self.fuel_level = fuel_level
	
	def max_dist(self):
		return self.fuel_level * self.mpg
		
	def move(self, distance):
		if (distance > self.max_dist()):
			#Google throw and catch exceptions in Python
			raise ValueError("Distance is beyond capacity")
		self.base_move(distance)
		burned = float(distance) / self.mpg
		print("Old Fuel Level: " + str(self.fuel_level))
		self.fuel_level -= burned
		print("New Fuel Level: " + str(self.fuel_level))
