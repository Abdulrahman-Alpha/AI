#     A program to convert liters to gallons

def main():

    print("This program converts liters to gallons.")

    gallons = eval(input("How many gallons? : "))
    liters = gallons * .264172052

    print("The fluid volume in liters is", liters, "liters.")
    input("Press the <Enter> key to quit.")
main();