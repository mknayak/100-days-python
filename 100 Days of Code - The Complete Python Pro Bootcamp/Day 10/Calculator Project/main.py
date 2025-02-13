import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2==0:
        return "NaN"
    return n1/n2

opDict = {"+":add,
          "-":subtract,
          "*":multiply,
          "/":divide}

def run_calc():
    print(art.logo)
    n1=float(input("What's your first number?:"))
    for op in opDict:
        print(op)
    continue_cal=True
    while continue_cal:
        operation= input("Pick an operation:")
        n2= float(input("what is the next number?:"))
        result=opDict[operation](n1,n2)
        print(f"{n1} {operation} {n2} = {result}")
        decision= input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        if decision=="y":
            n1=result
        else:
            run_calc()


run_calc()




