num1=int(input("enter the first number here: "))
num2=int(input("enter the second number here: "))
num3=int(input("enter the third number here: "))
if num1>num2 and num1>num3:
    print("the firsr number is big")
elif num2>num1 and num2>num3:
    print("the second number is big")
else:
    print("the third number is big")