def length(str):
    lis = list(str.split(" "))
    return len(lis[-1])

str = input("enter the string:")
print("The length of last word is",
      length(str))
