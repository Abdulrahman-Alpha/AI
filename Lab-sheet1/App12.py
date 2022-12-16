#.Write a Python program that finds the average of a series of numbers entered by the user. As in the previous problem, the program will first ask the user how many numbers there are. Note: The average should always be a float, even if the user inputs are all ints.
def main():
    n = int(input("Enter number : "))
    sum = 0
    # loop from 1 to n
    for num in range(1, n + 1, 1):
        sum = sum + num
    print("Sum of first ", n, "numbers is: ", sum)
    average = sum / n
    print("Average of ", n, "numbers is: ", average)
main()