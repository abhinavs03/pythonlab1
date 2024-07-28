largest=0
l=[]
n=int(input("Enter the no of elements:"))
for i in range(0,n):
    a=int(input("Enter the element:"))
    l.append(a)
largest=l[0]
for j in range(0,n):
    if l[j] > largest:
        largest=l[j]
    
print("Largest item:",largest)

'''
Enter the no of elements:5
Enter the element:2
Enter the element:1
Enter the element:3
Enter the element:6
Enter the element:4
Largest item: 6

'''
