#Question 5
class Vehicle:
	def __init__(self,size,weight):
		self.size=size
		self.weight=weight
	def Tire_size(self,Tire_size):
		print('Tire_size: ',Tire_size )
	def windows_count(self,windows_count):
		print('windows_count: ',windows_count)

class Car(Vehicle):
	def __init__(self,size,weight,Make,Model):
		Vehicle.__init__(self,size,weight)
		self.Make=Make
		self.Model=Model
	def color(self,color):
		print('color is:',color)


class BMW(Car):
	def __init__(self,size,weight,Make,Model,price,horsepower):
		Car.__init__(self,size,weight,Make,Model)
		self.price=price
		self.horsepower=horsepower
	def seat_color(self,seat_color):
		print('seat_color is:',seat_color)

my_bmw=BMW(25,1000,'BMW','Mseries',50000,1500)
my_bmw.Tire_size(50)
my_bmw.color('blue')
my_bmw.seat_color('brown')