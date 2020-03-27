print('function-args')
#case 1
def multiple(*ar):
	print(ar)
multiple(1,2,3,4)

def star(*a):
	for x in a:
		print(x)
star(10,20,30)