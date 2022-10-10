n1 = int(input("enter the first number:"))
n2 = int(input("enter the second number:"))
c = 0

for i in range(1, max(n1, n2) + 1): 
    if (n1 % i == 0) and (n2 % i == 0):
        c += 1

print(c)
