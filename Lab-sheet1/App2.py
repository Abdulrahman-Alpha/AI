#Write a Python program to perform a unit conversion of your own choosing. Make sure that the program prints an introduction that explains what it does.
#     A program to convert liters to gallons
def main():

    print("This program converts liters to gallons.")

    gallons = eval(input("How many gallons? : "))
    liters = gallons * .264172052

    print("The fluid volume in liters is", liters, "liters.")
    input("Press the <Enter> key to quit.")
main();