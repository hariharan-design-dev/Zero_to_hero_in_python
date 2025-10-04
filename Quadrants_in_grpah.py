x=float(input("enter the x axis values here: "))
y=float(input("entert the y axis value here:"))
if x==0.0 and y==0.0:
    print("the line is in the origin: ")
elif x>0 and y>0:
    print("the line is in the 1st quadrant")
elif x>0 and y<0:
    print("the line is in the 2nd quadrant ")
elif x<0 and y>0:
    print("the line is in the 3rd quadrant")
else:
    print("the line is in the 4th quadrant")