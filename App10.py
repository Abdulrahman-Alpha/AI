#Write a Python program to sum a series of numbers entered by the user. The program should first prompt the user for how many numbers are to be summed.  The program should then prompt the user for each of the numbers in turn and print out a total sum after all the numbers have been entered.
def main():
    n = int(input("Enter the number : ")) 
    sum = 0 
    for i in range ( n + 1 ): 
        sum = sum + i 
    print(f" The sum of the numbers from 1 to {n} is {sum}.")
main()