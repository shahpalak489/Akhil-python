# single inheritance
#parent class
class Father:
	def __init__(self,fname,lname):
		self.fname=fname
		self.lname=lname
	def printname(self):
		print(self.fname,self.lname)

x=Father('akhil','shah')
x.printname()

#to create child class
class Son(Father):
	pass
y=Son('palak','shah')
y.printname()


# Multiple Inheritance
#parentclass1
class Person:  
    #defining constructor  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  

    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
   
# defining another class  
#parentclass2
class Student: # Person is the  
    def __init__(self, studentId):  
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId  

#childclass  
class Resident(Person, Student): # extends both Person and Student class  
    def __init__(self, name, age, id):  
        Person.__init__(self, name, age)  
        Student.__init__(self, id)  
    
# Create an object of the subclass  
resident1 = Resident('John', 30, '102')  
resident1.showName()  
print(resident1.getId())  







'''

class Son2(Father):
	def __init__(self,midname):
		Father.__init__(self,fname,lname)
		self.midname=midname
	def printname(self):
		print(self.fname,self.lname)
z=Son2('akhil')
z.printname()
'''