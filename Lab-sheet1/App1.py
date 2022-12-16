#Write a Python program that converts distances measured in kilometers to miles. One kilometer is approximately 0.62 miles
kilometers = float(input("Enter value in kilometers: "))
# conversion factor
conv_fac = 0.621371
# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
