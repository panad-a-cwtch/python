num1 = input("Enter a whole number: ")
num2 = input("Enter a decimal number: ")

int_num = int(num1) 
float_num = float(num2)
round_num = int(round(float_num)) #Rounds number to nearest whole number.

print(int_num, float_num, round_num)
