# Write a Python program to find the sum of the first n natural numbers, where the value of n is provided by the user. 12. Write a program to find the sum of the cubes of the first n natural numbers where the value of n is provided by the user.
def sumOfSeries(n):
	sum = 0
	for i in range(1, n+1):
		sum +=i*i*i
		
	return sum
# Driver Function
n = 5
print(sumOfSeries(n))
 