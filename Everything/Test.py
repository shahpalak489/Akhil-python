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





out=[]
for x in range(100):
	if x %3 ==0:
		out.append(x)

out.sort(reverse=True)
print(out)


data=[5,7,9,11]
def incremental(values):
	length=len(values)
	diff=values[1]-values[0]
	for x in range(length-1):
		if values[x+1]-values[x]==diff:
			return True
	else:
		return False

nums=[2,3,7,11,15]
target=9

def same_as_target(values,target):
	for x in range(len(values)):
		for y in range(len(values)):
			if values[x]+values[y]==target:
				return [x,y]

final=same_as_target(nums,target)
print(final)



