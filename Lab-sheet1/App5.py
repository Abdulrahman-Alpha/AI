# Python program for slope of line
#Two points in a plane are specified using the coordinates (x1,y1) and (x2,y2). Write a Python program that calculates the slope of a line through two (non-vertical) points entered by the user.
# 𝑠𝑙𝑜𝑝 = 𝑦2 − 𝑦1 𝑥2 − 𝑥1
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
