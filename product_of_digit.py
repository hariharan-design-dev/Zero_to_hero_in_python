num=int(input("enter the digit:"))
digit_mul=1
while num>0:
    digit=num%10
    digit_mul*=digit
    num=num//10

print(f"the value of the digit multiplication is{digit_mul}")