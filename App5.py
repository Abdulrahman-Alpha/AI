# Python program for slope of line
def slope(x1, y1, x2, y2):
	if(x2 - x1 != 0):
	   return (float)(y2-y1)/(x2-x1)
	return sys.maxint


# driver code
x1 = 4
y1 = 2
x2 = 2
y2 = 5
print ("Slope is :", slope(x1, y1, x2, y2))
