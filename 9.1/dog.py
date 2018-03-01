class Dog(object):
	
	def __init__(self, name, age):
		self.name = name 
		self.age = age
	
	def sit(self):
		print(self.name.title() + ' is now sitting.')
	
	def roll_over(self):
		print(self.name.title() + ' rolled over!')
		
if __name__ == '__main__':
	d = Dog('Wang',2)
	d.sit()
	d.roll_over()
	
