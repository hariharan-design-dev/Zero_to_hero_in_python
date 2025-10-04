#in this code block we are going to see about how we calculate the count of even and odd numbers in the sequence of 10 values.
even_count=0
odd_count=0
for i in range(10):
    num=int(input("enter the values :"))
    if num%2==0 :
        even_count+=1
    else :
        odd_count+=1    
print("the even number count is",even_count)
print("the odd number count is ",odd_count)