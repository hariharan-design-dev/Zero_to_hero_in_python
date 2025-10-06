num = int(input("Enter the number: "))
sum = 0

for i in range(1, num + 1):
    if i % 2 != 0:
        sum += i

print(f"The sum of odd numbers from 1 to {num} is {sum}")
