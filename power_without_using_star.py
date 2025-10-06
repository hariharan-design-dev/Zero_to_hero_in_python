base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1
count = 0

while count < exponent:
    result *= base
    count += 1

print(f"{base} to the power of {exponent} is: {result}")
