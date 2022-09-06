a=str(input("enter the string:"))
s=("aeiou")
b=0
for i in a:
    if i in s:
        b=b+1
print(b)