minutes = int(input("Enter the total minutes: "))

hours = minutes // 60            
remaining_minutes = minutes % 60

print(f"{hours} hours {remaining_minutes} minutes")
