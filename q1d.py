smallest=0
l=[]
n=int(input("Enter the no of elements:"))
for i in range(0,n):
    a=int(input("Enter the element:"))
    l.append(a)
smallest=l[0]
for j in range(0,n):
    if l[j] < smallest:
        smallest=l[j]
    
print("smallest item:",smallest)

'''
Enter the no of elements:5
Enter the element:2
Enter the element:1
Enter the element:3
Enter the element:6
Enter the element:4
smallest item: 1
'''
