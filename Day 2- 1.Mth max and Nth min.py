a=int(input("enter the number of elements:"))
list1=[]
for i in range(0,a):
    ele=int(input("enter the elements:"))
    list1.append(ele)

final_list = []
M=int(input("enter the Mth max in list:"))
 
for i in range(0, M):
    j=max(list1)             
    list1.remove(j);
    final_list.append(j)
    a=min(final_list)  

final_list2 = []
N=int(input("enter the Nth min in list:"))
 
for i in range(0, N):
    k=min(list1)              
    list1.remove(k);
    final_list2.append(k)
    b=max(final_list2)  
print("Sum=",a+b)
print("Difference=",a-b)

