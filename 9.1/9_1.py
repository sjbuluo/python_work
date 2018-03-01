class Restaurant(object):
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print(self.restaurant_name, self.cuisine_type)
		
	def open_restaurant(self):
		print(self.restaurant_name, 'open')
	
r = Restaurant('A',1)

r.describe_restaurant()

r.open_restaurant()
