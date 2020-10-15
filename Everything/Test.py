#Question 5
class Vehicle:
	vehicle_class='4 wheeler'			
	def __init__(self,Vehicle1,Vehicle2):
		self.Vehicle1=Vehicle1
		self.Vehicle2=Vehicle2
	def method1(self,Vehicle3):
		print('method1')
	def method2(self,Vehicle4):
		print('method2')

class Car(Vehicle):
	Car_class='Honda'	
	def __init__(self,Vehicle1,Vehicle2,Car1,Car2):
		Vehicle.__init__(self,Vehicle1,Vehicle2)
		self.Car1=Car1
		self.Car2=Car2
	def method3(self,Car3):
		print('method3')
	def method4(self,Car4):
		print('method4')

class BMW(Car):
	vehicle1='4 wheeler'			
	vehicle2='2 wheeler'
	def __init__(self,Vehicle1,Vehicle2,Car1,Car2,BMW1,BMW2):
		Car.__init__(self,Vehicle1,Vehicle2,Car1,Car2)
		self.BMW1=BMW1
		self.BMW2=BMW2
	def method5(self,BMW3):
		print('method5')
	def method6(self,BMW4):
		print('method6')


my_bmw=BMW('big','small','tesla','Benz','Series4','series5')
my_bmw.method6('series6')
my_bmw.method4('series6')
my_bmw.method2('series6')