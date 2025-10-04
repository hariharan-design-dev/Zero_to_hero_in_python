unit=int(input("enter the units consumed :"))

if unit < 100:
    total_cost=unit*5
elif unit > 100:
    total_cost=unit*7
else:
    print("enter the correct unit readings")

print(f"the total rupees is {total_cost}")
    