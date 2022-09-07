a = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1,a):
    if(a % i == 0):
        Sum = Sum + i
if (Sum ==a):
    print(" %d is a Perfect Number" %a)
elif(a<0):
    print("Invalid Input")
else:
    print(" %d is not a Perfect Number" %a)