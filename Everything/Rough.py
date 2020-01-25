#ex 8
s='hi ratan sor how are you ?'
#method 1
def m1(x):
	y=x.split(' ')
	print(y)
	for z in y:
		print(len(z))
m1(s)

#method 2
words=s.split()
print(list(map(lambda x:len(x),words)))
