from functools import reduce

#15.1 Use map, takes number and return square of each number
NumSquare = lambda Num : (Num**2)

#15.2 Use Filter, takes number and return Even out of them
EvenNum = lambda Num : (Num % 2 == 0)

#15.3 Use Filter, takes number and return Odd out of them
OddNum = lambda Num : (Num % 2 != 0)

#15.4 Use reduce, addition of all numbers
Add = lambda A,B : A+B

#15.5 Use reduce, find Max of all numbers
MaxNum = lambda A,B : (A if (A>B) else B)

#15.6 Use reduce, find Min of all numbers
MinNum = lambda A,B : (A if (A<B) else B)

#15.7 Use filter to return strings length greater than 5
StrinLength5 = lambda string : (len(string) > 5)

#15.8 Use filter to return number that is divisible by 3 & 5
Divi3and5 = lambda Num : (Num % 3 == 0) and (Num % 5 == 0 )

#15.9 Use reduce to return product of all elements in list
Prod = lambda A,B : A*B

#15.10 Use filer to return count of even numbers
EvenCount = lambda Num : (Num % 2 == 0)

def main():
    Data = [1,2,3,4,15,6,7,8,9,10]
    Strings = ["Three","Six","Clear","Eleven","Thirteen","Seventeen","Hundred"]

    MapData = list(map(NumSquare, Data))
    print("Data after square of each number is:",MapData)
    print("----------------------------------------------")
    print("Actual Data is :", Data)
    FilterData = list(filter(EvenNum, Data))
    print("Filtered data for Even number is :",FilterData)
    print("----------------------------------------------")
    print("Actual Data is :", Data)
    FilterData = list(filter(OddNum, Data))
    print("Filtered data for Odd number is :",FilterData)
    print("----------------------------------------------")
    print("Actual Data is :", Data)
    RData = reduce(Add, Data)
    print("Addition of all numbers using reduce is :",RData)
    print("----------------------------------------------")
    print("Actual Data is :", Data)
    RData = reduce(MaxNum, Data)
    print("Max of all numbers using reduce is :",RData)
    print("----------------------------------------------")
    print("Actual Data is :", Data)
    RData = reduce(MinNum, Data)
    print("Min of all numbers using reduce is :",RData)
    print("----------------------------------------------")
    FilterString = list(filter(StrinLength5, Strings))
    print("String data more length more than five:",FilterString)
    print("----------------------------------------------")
    FilterNum = list(filter(Divi3and5,Data))
    print("Number Divisible by 3 and five:",FilterNum)
    print("----------------------------------------------")
    ReduceProd = reduce(Prod,Data)
    print("Prod of all elements:",ReduceProd)
    print("----------------------------------------------")
    FilterEvenCount = list(filter(EvenCount,Data))
    CountData = len(FilterEvenCount)
    print("Count of all even elements:",CountData)


if __name__ == "__main__":
    main()