#Inside Arithmetic module

#17.1

def Add(Num1, num2):
    Sum = 0
    Sum = Num1 + num2
    return Sum

def Sub(Num1,Num2):
    Sub = 0
    Sub = Num1 - Num2
    return Sub

def Multiplication(Num1,Num2):
    Mult = 0
    Mult = Num1 * Num2
    return Mult

def Division(Num1,Num2):
    Div = Num1 / Num2
    return Div

#17.3 Factorial of given number
def Factorial(Num):
    Fact = 1
    for i in range(1,Num+1):
        Fact = Fact * i
    return Fact

#17.4 Sum of Factors of given number
def Factor(Num):
    Fact = 1
    Sum = 0
    for i in range (1,Num):
        if (Num % i == 0):
            Sum = Sum + i
    return Sum

#17.5 Check if its prime number or not
def Prime(Num):
    for i in range (2,Num):
        if (Num % i == 0 ):
            #print(i)
            return f"{Num} is not prime number"
    return f"{Num} is prime number"

#17.9 Sum of the number accepted from user
def NumberOfDigit(Num):
    Data = []
    strNum = str(Num)
    Sum = 0
    for i in strNum:
        Sum = Sum + int(i)
    return Sum

#17.10 Count of digits from number accepted from user
def CountOfDigit(Num):
    Data = []
    strNum = str(Num)
    Sum = 0
    for i in strNum:
        #print(i)
        Sum = Sum + int(i)
        Data.append(i)
    return(Data)