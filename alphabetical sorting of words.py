a=str(input("Enter the text:"))
b=[i.lower()for i in a.split()]
b.sort()
print("The sorted words are:")
for i in b:
    print(i)