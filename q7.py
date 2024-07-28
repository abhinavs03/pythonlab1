import math
def area_of_tri(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a1 = float(input("Enter the first side of the first triangle: "))
b1 = float(input("Enter the second side of the first triangle: "))
c1 = float(input("Enter the third side of the first triangle: "))

a2 = float(input("Enter the first side of the second triangle: "))
b2 = float(input("Enter the second side of the second triangle: "))
c2 = float(input("Enter the third side of the second triangle: "))

area1 = area_of_tri(a1, b1, c1)
area2 = area_of_tri(a2, b2, c2)

tot_area = area1 + area2

contr1 = (area1 / tot_area) * 100
contr2 = (area2 / tot_area) * 100

print("Area of the first triangle is:", area1)
print("Area of the second triangle is:",area2)
print("Total area enclosed by both triangles is:",tot_area)
print("First triangle contributes ",contr1,"% to the total area.")
print("Second triangle contributes ",contr2,"% to the total area.")



'''
Enter the first side of the first triangle: 3
Enter the second side of the first triangle: 4
Enter the third side of the first triangle: 5
Enter the first side of the second triangle: 12
Enter the second side of the second triangle: 13
Enter the third side of the second triangle: 15
Area of the first triangle is: 6.0
Area of the second triangle is: 74.83314773547883
Total area enclosed by both triangles is: 80.83314773547883
First triangle contributes  7.422697455299658 % to the total area.
Second triangle contributes  92.57730254470034 % to the total area.
'''
