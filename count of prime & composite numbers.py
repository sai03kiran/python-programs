a=int(input("Enter any number:"))
p=0
c=0
if(a==0 or a==1):
    print("0 and 1 are neither prime nor composite")
elif(a<0):
    print("Invalid input")
elif(a>=2):
    for i in range(2,a+1):
        if(i%2!=0):
            p+=1
        else:
            c+=1
print("count of prime numbers:",p)
print("count of composite numbers:",c)