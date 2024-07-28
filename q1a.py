s = 0
l = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    a = int(input(f"Enter element: "))
    l.append(a)
for j in l:
    s += j
print("Sum of items:", s)

'''
Enter the number of elements in the list: 5
Enter element: 2
Enter element: 1
Enter element: 3
Enter element: 6
Enter element: 4
Sum of items: 16
'''
