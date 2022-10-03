a=int(input("Enter the number of fresh loaves:"))
b=int(input("Enter the number day old loaves:"))
a=a*185
b=b*185
if(a>=0 and b>=0):
    print("The regular price of loaves:Rs.185")
    print("The amount of new loaves is: %0.2f"%(a))
    print("The amount of day old loaves is: %0.2f"%(b*0.6))
    print("The total amount:Rs.%0.2f"%(a+(b*0.6)))
else:
    print("Invalid input")
