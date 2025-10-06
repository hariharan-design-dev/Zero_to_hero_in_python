num = int(input("Enter a number: "))
original = num
order = len(str(num))     
armstrong_sum = 0     

while num != 0:
    digit = num % 10
    armstrong_sum += digit ** order 
    num = num // 10                 


if original == armstrong_sum:
    print(f"{original} is an Armstrong Number ")
else:
    print(f"{original} is NOT an Armstrong Number ")
