print("the mark sheet contains the total & average of the 5 subjects ")
tamil=float(input("enter the mark scored in tamil subject:"))
english=float(input("enter the mark scored in the english subject:"))
maths=float(input("enter the mark scored in maths subject:"))
science=float(input("enter the mark scored in science subject:"))
social=float(input("enter the mark scored in social subject:"))
total_mark=tamil+english+maths+science+social
average=total_mark/5
print(f"the total mark scored out of 500 is{total_mark:.2f}& the average in class 10 grade is{average:.2f}")