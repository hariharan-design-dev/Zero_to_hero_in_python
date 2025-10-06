num = int(input("Enter the number: "))
original = num        
reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10


if original == reverse:
    print("The given number is a palindrome ")
else:
    print("The given number is not a palindrome ")

print(f"The reversed number is: {reverse}")
