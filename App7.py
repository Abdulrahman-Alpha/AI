def main():
    cof = 10.50
    ship = 0.86
    ovh = 1.50
    pds = eval(input("How many pounds of coffee? "))
    ans = ovh + (cof*pds) + (ship*pds)
    print("The cost of your order would equal $",ans)
main()
    