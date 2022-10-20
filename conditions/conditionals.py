mark = int(input("Enter your mark: "))

if mark >= 70:
    print("Distinction!")
elif mark >= 60 and mark <70:
     print("Merit")
elif mark >= 40 and mark <60:
    print("Pass")
else:
    print("Fail")
    