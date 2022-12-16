#####################sheet2#######################
#----------------------------- script 1
import numpy 
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)
# this script will calculate the mean of the list speed which is equal to (89.76923076923077)
#------------------------------ script 2 
import numpy 
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)
# this script will calculate the median of the list speed which is equal to 87.0.
#----------------------------- script 3
import numpy 
speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)
# this script will calculate the median of the list speed which is equal to 86.5 
#----------------------------- script 4
from scipy import stats 
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)
# this script will calculate the mode of the list speed which will equal to 86.0
#------------------------------ script 5
import numpy 
speed = [86,87,88,86,87,85.86]
x = numpy.std(speed)
print(x)
# this script will calculate the standard deviation of the list speed which will equal to 0.9035079029052513
#------------------------------ script 6
import numpy 
speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)
# this script  will calculate the variance of the list speed which will equal to 1432.2448979591834 .
#----------------------------- script 7
import numpy 
x= numpy.random.uniform(0.0,5.0,250)
print(x)
#this script will create arrays filled with random samples which are from a uniform distribution.
#---------------------------- script 8
import numpy 
import matplotlib.pyplot as plt 
x= numpy.random.uniform(0.0,5.0,1000)
plt.hist(x,100)
plt.show()
#this script will appear polygram in a figure with random values in an array
# ----------------------------- script 9
import numpy 
import matplotlib.pyplot as plt 
x= numpy.random.normal(5.0,1.0,1000)
plt.hist(x,100)
plt.show()  
#this script will appear polygram in a figure with random values in an array
#----------------------------- script 10
import matplotlib.pyplot as plt 
x= [5,7,8,7,2,17,2,9,4,11,12,9,6]
y= [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x,y)
plt.show()  
# this script will appear a points with positions x , y  in the figure 