numA = int(input("Enter number a: "))
numB = int(input("Enter number b: "))
numC = int(input("Enter number c: "))

if numA > numB:
    if numA > numC:
        print(numA)
    else:
        print(numC)
elif numB > numC:
    print(numB)
else:
    print(numC)
        