#A coffee shop sells coffee at $10.50 a pound plus the cost of shipping. Each order ships for $0.86 per pound + $1.50 fixed cost for overhead. Write a Python program that calculates the cost of an order.
def main():
    cof = 10.50
    ship = 0.86
    ovh = 1.50
    pds = eval(input("How many pounds of coffee? "))
    ans = ovh + (cof*pds) + (ship*pds)
    print("The cost of your order would equal $",ans)
main()
    