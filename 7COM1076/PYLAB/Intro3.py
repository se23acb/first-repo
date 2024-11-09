def doSomeCal(x,y):
    sum = x + y
    division = x / y 
    product_of_xy = x * y
    printCalc(sum,division,product_of_xy)

def printCalc(sum,division,product_of_xy):
    print("Sum", sum)
    print("Division", division)
    print("product", product_of_xy)


def main():
    doSomeCal(100,200)
   

if __name__ == "__main__":
    main()


