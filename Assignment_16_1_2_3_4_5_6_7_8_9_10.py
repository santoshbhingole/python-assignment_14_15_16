#16.1 print Hello from function
def fun():
    print("Hello from Fun")

#16.2 Return if number is Even or Odd
def EvenOdd(Num):
    if (Num % 2  == 0):
        return f"Even Number"
    else:
        return f"Odd Number"
#16.3 Return Sum of the number
def Add(Num1, Num2):
    Sum = Num1 + Num2
    return Sum

#16.4 Display Marvellous on screen five times
def Display(Num):
    for i in range (Num):
        print ("Marvellous")
        
#16.5 Display 10 to 1 reverse order
def Display1(Num):
    Data = []
    for i in range (Num, 0, -1):
        #print(i)
        Data.append(i)
    return Data

#16.6 Display "*" on screen five times
def DisplayStar(Num):
    Data = []
    for i in range (Num):
        print("*")
        Data.append(i)
    return Data

#16.7 Display if number is positive or Negative
def PosNeg(Num):
    if (Num == 0):
        return f"Zero"
    while (Num < 0):
        return f"Negative number"
    else:
        return f"Positive number"
    
#16.8 Display first 10 even numbers on screen
def DisplayEven(Num):
    Data = []
    for i in range (0, Num+1):
        if (i % 2 == 0):
            Data.append[i]
            print(i)

#16.9 Display first 10 even numbers on screen
def DisplayEven(Num):
    Data = []
    Count = 0
    for i in range (2, Num+1):
        if (i % 2 == 0):
            Data.append(i)
    return Data

#16.10 Display number of char in given string
def LengthName(str):
    Data = []
    for i in str:
        #print(i)
        Data.append(i)
    return Data
    
def main():
    print("-----------------------------------")
    fun()
    print("-----------------------------------")
    Num = int(input("Enter the number of Even/Odd validation :"))
    Result = EvenOdd(Num)
    print(Result)
    print("-----------------------------------")
    Num1 = int(input("Enter the first Number :"))
    Num2 = int(input("Enter the Second Number :"))
    Ret = Add(Num1, Num2)
    print("Addition of the two number is :",Ret)
    print("-----------------------------------")
    Ret = Display(5)
    print("-----------------------------------")
    Ret = Display1(10)
    print(Ret)
    print("-----------------------------------")
    Ret = DisplayStar(5)
    print("-----------------------------------")
    Num = int(input("Enter the number for postive/Negative validation :"))
    Ret = PosNeg(Num)
    print(Ret)
    print("-----------------------------------")
    Ret = DisplayEven(20)
    print("First 10 even numbers are :",Ret)
    print("-----------------------------------")
    ret = LengthName("Marvellous")
    print("Length of given string 'Marvellous' is :", len(ret))


if __name__ == "__main__":
    main()

