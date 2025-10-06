n = int(input("Enter the value of n: "))

print("The even numbers from 1 to", n, "are:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
