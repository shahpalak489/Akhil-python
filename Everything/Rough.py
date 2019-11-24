List1=(1,2,3,4,5)

list2={i:i*2 for i in List1}
#print(list2)

list3={1: 2, 2: 4, 3: 6, 4: 8, 'a': 10}
r=list3['a']
r=list3.keys()
r=list3.values()
r=list3.items()
print(r)

for i in list3.keys():
	print(i)

for i in list3.values():
	print(i)

for i in list3.items():
	print(i)

for key,value in list3.items():
	print(key,'<>',value)

