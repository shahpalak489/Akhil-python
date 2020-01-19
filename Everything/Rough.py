def outer():
	name1='ratan'
	def inner():
		#nonlocal name1
		name1='durga'
		print(name1)
	print(name1) 
	inner()
	print(name1)

outer()
