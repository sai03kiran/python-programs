list=[]
b=int(input("enter the no of elements:"))
p=0
c=0
for i in range(1,b+1):
    d=int(input("enter the number:"))
    if(d==1):
        print("1 is neither prime nor composite")
    list.append(b)
    if(i%2!=0):
        p=p+1
    else:
        c=c+1
print("The count of prime numbers are:",p)
print("The count of composite numbers are:",c)