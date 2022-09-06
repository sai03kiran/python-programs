def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
a=int(input("select any operation:-\n"
        "1.addition\n"
        "2.subtracdtion\n"
        "3.multiplication\n"
        "4.division\n"))
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
if(a==1):
    print(n1,"+",n2,"=",add(n1,n2))
elif(a==2):
    print(n1,"-",n2,"=",sub(n1,n2))
elif(a==3):
    print(n1,"*",n2,"=",mul(n1,n2))
elif(a==4):
    print(n1,"/",n2,"=",div(n1,n2))
else:
    print("Invalid input")