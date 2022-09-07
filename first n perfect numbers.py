a=int(input("Enter any number: "))
print("The first",a,"perfect numbers are:")
for Number in range(1,a- 1):
    Sum = 0
    for n in range(1, Number - 1):
        if(Number % n == 0):
            Sum = Sum + n
    if(Sum == Number):
        print("%d " %Number)