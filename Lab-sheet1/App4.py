#Write a Python program that computes the molecular weight of a carbohydrate (in grams per mole) based on the number of hydrogen, carbon, and oxygen atoms in the  molecule. The program should prompt the user to enter the number of hydrogen atoms, the number of carbon atoms, and the number of oxygen atoms. The program then prints the total combined molecular weight of all the atoms based on these individual atom weights : 
# Atom Weight
# _______(grams I mole) 
#  H 1.00794 
#  C 12.0107 
#  0 15.9994 
# For example, the molecular weight of water (H20) is : 
# 2(1.00794) + 15.9994 = 18.01528
def main():
    print("This program finds the total molecular weight of a combination of hydrogen, carbon and oxygen atoms (Try H2O)")
    h = eval(input("How many hydrogen atoms? "))
    c = eval(input("Carbon? "))
    o = eval(input("Oxygen? "))
    total = (h * 1.00794) + (c * 12.0107) + (o * 15.9994)
    print("The total molecular weight is", total)

main()