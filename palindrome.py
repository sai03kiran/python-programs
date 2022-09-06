a=str(input("enter the text:"))
a=a.casefold()
b=reversed(a)
if list(a)==list(b):
    print("The entered text is a palindrome")
else:
    print("The entered text is not a palindrome")