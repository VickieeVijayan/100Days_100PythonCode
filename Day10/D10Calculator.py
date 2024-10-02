from D10art import logo

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

calculatorDic = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def Calculator():
    print(logo)
    Calculation = True
    num1 = float(input("What's the First Number? : "))

    while Calculation:
        operator = input("+ \n-\n*\n/\n"
                         "Pick an operation: ")
        num2 = float(input("What's the Second Number? : "))
        result = calculatorDic[operator](num1, num2)
        print(f"calculation: {num1} {operator} {num2} = {result}")
        Choice = input("Type 'y' to continue calculating"
                     f"with {result}, or Type 'n' to start new calculation.").lower()
        if Choice == "n":
            Calculation = False
            print("\n" * 20)
            Calculator()
        elif Choice == "y":
            num1 = result

Calculator()