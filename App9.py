from math import *
def main():
    height = eval(input("Please enter the height of the ladder "))
    deg = eval(input("Please enter the angle of the ladder in degrees "))
    rad = (pi/180) * deg
    leng = height/(sin(rad))
    print("The length of the ladder must be ", leng)
main()