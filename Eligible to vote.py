a=int(input("Enter the person's age:"))
if(a>=18):
    print("person is eligible to vote")
elif(a<18 and a>0):
    print("You are allowed to vote after",18-a,"years")
else:
    print("Invalid Input")
