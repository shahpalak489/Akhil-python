 





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