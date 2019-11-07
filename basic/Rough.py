# first 100 numbers
for i in range(0,100):
	print(i)

# all even numbers till 100
for i in range(100):
	if i%2 ==0:
		print(i)
#even numbers without modules

#fibonnaci first 10 with generator


# Revert Dictioanry mapping
map1={'a':1,'b':2}

map2={y:x for x,y in map1.items()}
print(map2)
