num=int(input("enter the fact value: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
    #1=1*1
    #1=1*2
    #2=2*3
    #6=6*4
    #24=24*5 ------>120 and the loop reach its end and terminalte the loop
print(f"the factorial value is{fact}")
