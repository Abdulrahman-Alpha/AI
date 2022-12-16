#Python Program to find the area of triangle
#Write a Python program to calculate the area of a triangle given the length of its three sides-a, b, and c-using these formulas : 
# 𝑠 = 𝑎 + 𝑏 + 𝑐 2 𝐴 = √𝑠(𝑠 − 𝑎)(𝑠 − 𝑏)(𝑠 − 𝑐)
def main():
    a = float(input('Enter first side: '))
    b = float(input('Enter second side: '))
    c = float(input('Enter third side: '))
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("The area of the triangle is %0.2f" %area)
main()