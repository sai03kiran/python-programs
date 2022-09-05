n=int(input("enter a number:"))
a=0
b=1
if(n<0):
    print("Invalid input")
elif(n==0):
    print("0")
elif(n==1):
    print("1")
else:
    for i in range(1,n):
        c=a+b
        a=b
        b=c
    print("The fibonacci of the number is:",b)