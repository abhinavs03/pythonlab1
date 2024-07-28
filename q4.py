ListColour= [["Black", "Red", "Maroon", "Yellow"], ["000000", "FF0000",
"800000", "FFFF00"]]
key=["colorName","colorCode"]
n=len(ListColour[0])
ListDict=[]
for i in range(0,n):
    ListDict.append({key[0] : ListColour[0][i], key[1] : ListColour[1][i]})
print(str(ListDict))    
    

'''       [{'colorName': 'Black', 'colorCode': '000000'}, {'colorName': 'Red', 'colorCode': 'FF0000'}, {'colorName': 'Maroon', 'colorCode': '800000'}, {'colorName': 'Yellow', 'colorCode': 'FFFF00'}]         '''


