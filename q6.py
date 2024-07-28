while True:
    num = input("Enter a four-digit number: ")
    if num.isdigit() and len(num) == 4:
        num = int(num)
        break
    else:
        print("Invalid input....")
num = str(num)
s = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
rev = int(num[::-1])
print("Sum of the digits is: ",s)
print("Reverse of the number is: ",rev)


'''
Enter a four-digit number: 2435
Sum of the digits is:  14
Reverse of the number is:  5342
'''
