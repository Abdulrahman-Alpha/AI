def main():
    print("This program finds the total molecular weight of a combination of hydrogen, carbon and oxygen atoms (Try H2O)")
    h = eval(input("How many hydrogen atoms? "))
    c = eval(input("Carbon? "))
    o = eval(input("Oxygen? "))
    total = (h * 1.00794) + (c * 12.0107) + (o * 15.9994)
    print("The total molecular weight is", total)

main()