n=int(input("Enter any number:"))
if(n==0):
    print("Zero is neither odd nor even")
elif (n % 2 == 0):
    print("The entered number is even")
else:
    print("The entered number is odd")