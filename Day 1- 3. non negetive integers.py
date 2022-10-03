n = int(input("enter the number of items in list:"))
A=[]
for i in range(n):
    b=int(input("enter the items of list:"))
    A.append(b)
print(A)
l1 = len(A)
area = 0
for i in range(l1) :
      for j in range(i + 1, l1) :
        area = max(area, min(A[j], A[i]) * (j - i))
print(area)
