# Write a Python program to determine the length of a ladder required to reach a given height when leaned against a house. The height and angle of the ladder are given as inputs. To compute length use : 
# 𝑙𝑒𝑛𝑔𝑡ℎ = ℎ𝑒𝑖𝑔ℎ𝑡
# sin 𝑎𝑛𝑔𝑙𝑒
# Note: The angle must be in radians. Prompt for an angle in degrees and use this formula to convert : 
# 𝑟𝑎𝑑𝑖𝑎𝑛𝑠 = 𝜋
# 180 𝑑𝑒𝑔𝑟𝑒�
from math import *
def main():
    height = eval(input("Please enter the height of the ladder "))
    deg = eval(input("Please enter the angle of the ladder in degrees "))
    rad = (pi/180) * deg
    leng = height/(sin(rad))
    print("The length of the ladder must be ", leng)
main()