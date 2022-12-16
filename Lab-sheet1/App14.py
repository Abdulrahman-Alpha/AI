#A Fibonacci sequence is a sequence of numbers where each successive number is  the sum of the previous two. The classic Fibonacci sequence begins: 1, 1, 2, 3, 5, 8, 13, .... Write a Python program that computes the nth Fibonacci number where n is a value input by the user. For example, if n = 6, then the result is 8
def fibonacci(n):
	if n <= 1:
		return n
	return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
	n = 6
	print(fibonacci(n))
