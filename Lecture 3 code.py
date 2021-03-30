def expbyreduce2 (x,y):
	xlist = [x]*y
	def mult(a,b):
		return a*b
	return reduce(mult,xlist)
