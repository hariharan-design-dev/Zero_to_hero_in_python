# this problem is an loop based one what we going to see in this is we are going to find the power values of the number, for example 2^3=8, 2*2*2=8 like wise we going to see this one in the program based one.
base=int(input("enter the base value : "))
power=int(input("enter the the power value : "))
#in this part only the actual calculation begins.
result=1#because in the calculation if we use zero means all the multiplied value is become zero so only we use the 1.
# the actuall the forloop condition is 
for i in range (power):
    result=result*base # how this part actually working is ,our result value is 1 so the condition we initiate is result=result*base
    #1=1*2----> 1st iteration.
    #2=2*2---->2nd iteration.
    #4=4*2---->3rd iteration.
    
print("the exponent value is :",result)
    

