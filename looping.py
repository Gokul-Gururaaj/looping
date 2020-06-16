list=[]
list1=[]
n=int(input("enter the len of the list"))
print("enter the no's")
for i in range(n):
    data=int(input())
    list.append(data)
    if(list[i]>0):
        list1.append(data)
print("Your list=",list)
            
print("The postive no's in it",
      list1)
