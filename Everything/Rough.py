#print("***to create class")
class House:
	pass

#print("instance variable")
class Employee:
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email= first + '.' + last + "@company.com"

	def fullname(self):
		return self.first

emp1= Employee('kartik','patel',5000)
emp2=Employee('Hari','gotipatti',10000)

print(emp1.email)
print(emp2.email)
print(emp2.fullname)

12:00 






#print("class variable")
class MyClass:
  x = 5

#print("***to create object")
p1 = MyClass()
print(p1.x)
