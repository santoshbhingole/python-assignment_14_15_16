#14.1 Lambda function to calcualte square of number
Square = lambda A: (A*A)

#14.2 Cube of number
Cube = lambda A: (A**3)

#14.3 Return Max Num out of 2 numbers
MaxNum = lambda A,B: f"{A} is MaxNum" if A > B else f"{B} is MaxNum"

#14.4 Return Minimum Num out of 2 numbers
MinNum = lambda A,B: f"{A} is MinNum" if A < B else f"{B} is MinNum"

#14.5 Return True if number is even
Even = lambda A: True if (A % 2 == 0) else False

#14.6 Return True if number is odd
Odd = lambda A: True if (A % 2 != 0) else False

#14.7 Return True if number is divisible by 5
Divby5 = lambda A: True if (A % 5 == 0) else False

#14.8 Return Addition of two numbers
Add = lambda A,B : A+B

#14.9 Multiplication of two numbers
Mul = lambda A,B : A*B

#14.10 Max out of three numbers
MaxOf3 = lambda A,B,C : (
    "A is larger number" if (A > B and A > C) 
    else "B is largest number" if (B > C) 
    else "C is largest number" ) 

def main():
    Ret = Square(5)
    print("Square of the number is :", Ret)

    Ret = Cube(5)
    print("Cube of the number is :", Ret)

    Ret = MaxNum(100,12)
    print("MaxNum is:", Ret)

    Ret = MinNum(100,12)
    print("MinNum is :", Ret)

    Ret = Even(10)
    print("Number is Even Number :",Ret)

    Ret = Odd(11)
    print("Number is Odd Numer :",Ret)

    Ret = Divby5(25)
    print("Number is Divisible by 5 :",Ret)

    Ret = Add(10,20)
    print("Addition of number is:",Ret)

    Ret = Mul(10,20)
    print("Multiplication of two number is:",Ret)

    Ret = MaxOf3(50,40,60)
    print("Max of three number is:",Ret)
if __name__ == "__main__":
    main()