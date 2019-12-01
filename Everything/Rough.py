#https://www.youtube.com/watch?v=ZDa-Z5JzLYM
#print("***to create class")
class House:
	pass

#print("instance variable")
class Employee:
	def __init__(self,first2,last2,pay2):
		self.first1=first2
		self.last1=last2
		self.pay1=pay2
		self.email1= first2 + '.' + last2 + "@company.com"

	def fullname(self):
		return self.first1

emp1= Employee('kartik','patel',5000)
emp2=Employee('Hari','gotipatti',10000)

print(emp1.email1)
print(emp2.email1)
print(emp2.fullname())

#print("class variable")
class MyClass:
  x = 5

#print("***to create object")
p1 = MyClass()
print(p1.x)
