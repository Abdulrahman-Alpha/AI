#Write a Python program that accepts two points (see previous problem) and determines the distance between them. 
# 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒 = √(𝑥2 − 𝑥1)2 + (𝑦2 − 𝑦1)2
import math 
def main():
    p1 = [4, 0]
    p2 = [6, 6]
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    print(distance)
main()