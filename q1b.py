m=1
l=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    a=int(input("Enter the element:"))
    l.append(a)
for j in l:
    m*=j
print("Product:",m)

'''
Enter the number of elements in the list:5
Enter the element:2
Enter the element:1
Enter the element:3
Enter the element:6
Enter the element:4
Product: 144
'''
