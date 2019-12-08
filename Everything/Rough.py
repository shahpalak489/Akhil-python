

def akhil(n):
	result=""
	if n % 3 == 0:
		return 'AB'
	elif n % 3 == 1:
		return 'cd'
	else:
		return 'ef'

ak=akhil(10)
print(ak)
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