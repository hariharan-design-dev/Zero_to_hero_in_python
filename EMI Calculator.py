principal = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period in years: "))


monthly_rate = annual_rate / (12 * 100)
months = time * 12

EMI = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
print(f"The EMI amount to be paid per month is: ₹{EMI:.2f}")
