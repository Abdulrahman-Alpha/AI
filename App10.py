def main():
    n = int(input("Enter the number : ")) 
    sum = 0 
    for i in range ( n + 1 ): 
        sum = sum + i 
    print(f" The sum of the numbers from 1 to {n} is {sum}.")
main()