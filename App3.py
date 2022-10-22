#Write a Python program to calculate the volume and surface area of a sphere from 
# its radius, given as input. Here are some formulas that might be useful : 
# 𝑉 = 4/3 * 𝜋𝑟^3, 𝐴 = 4 * 𝜋𝑟^2
def main():
   pi=22/7
   radian = float(input('Radius of sphere: '))
   sur_area = 4 * pi * radian **2
   volume = (4/3) * (pi * radian ** 3)
   print("Surface Area is: ", sur_area)
   print("Volume is: ", volume)
main()