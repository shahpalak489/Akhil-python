#example 10  			# class variable value is related to each object  

class Myclass():
	name='ratan'

c1=Myclass()
c2=Myclass()

print(c1.name)			#ratan

c1.name='durga'
print(c1.name)			#durga		

print(c2.name)			#ratan	 #c1.name is different than c2.name so when we chnage c1.name its doesnt affect c2.name