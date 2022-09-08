n=int(input("Enter the number:"))
org=n
sum=0
while(n>0):
    a=n%10
    sum=sum*10+a
    n=n//10
print("Reverse of number is:",sum)