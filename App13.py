#You have seen that the math library contains a function that computes the square root of numbers. In this exercise, you are to write your own algorithm for computing square roots. One way to solve this problem is to use a guess-and -check approach. You first guess what the square root might be, and then see how close your guess is. You can use this information to make another guess and continue guessing until you have found the square root (or a close approximation to it). One particularly good way of making guesses is to use Newton's method. Suppose x is  the number we want the root of, and guess is the current guessed answer. The guess can be improved by using computing the next guess as: 
# 𝑔𝑢𝑒𝑠𝑠 + 𝑥
# 𝑔𝑢𝑒𝑠𝑠
# 2
# Write a Python program that implements Newton's method. The program should prompt the user for the value to find the square root of (x) and the number of  times to improve the guess. Starting with a guess value of x/2, your program should loop the specified number of times applying Newton's method and report  the final value of guess. You should also subtract your estimate from the value of math. sqrt (x) to show how close it is.
def squareRoot(n, l) :
	# Assuming the sqrt of n as n only
	x = n

	# To count the number of iterations
	count = 0

	while (1) :
		count += 1

		# Calculate more closed x
		root = 0.5 * (x + (n / x))

		# Check for closeness
		if (abs(root - x) < l) :
			break

		# Update root
		x = root

	return root
if __name__ == "__main__" :

	n = int(input("Enter the intger number :  "))# 16
	l = float(input("Enter the tolerance level : "))# 0.00001

	print( "the root is equal to : ",squareRoot(n, l))
