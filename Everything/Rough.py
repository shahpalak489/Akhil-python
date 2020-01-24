# ex 5				
#map			#perform operation on all elements
l1=[2,3,4]

def m1(x):
	return x*5
print(list(map(m1,l1)))
print(list(map(lambda x:x*5,l1)))