people_info = [
    {"name":"John","age": 28, "blood_group": "A+"},
    {"name":"Jane","age": 22, "blood_group": "B+"},
    {"name":"Mike","age": 32, "blood_group": "O-"},
    {"name":"Anna","age": 25, "blood_group": "AB+"},
    {"name":"Tom","age": 30, "blood_group": "A-"},
    {"name":"Sara","age": 27, "blood_group": "B-"},
    {"name":"Paul","age": 24, "blood_group": "O+"},
    {"name":"Kate", "age": 29, "blood_group": "AB-"},
    {"name":"Chris", "age": 26, "blood_group": "A+"},
    {"name":"Nina","age": 23, "blood_group": "B+"}
]

for i in people_info:
    print("Name: ",i["name"])
    print("Age: ",i["age"])
    print("Blood Group: ",i["blood_group"])
    print("-" * 20)



'''
Name:  John
Age:  28
Blood Group:  A+
--------------------
Name:  Jane
Age:  22
Blood Group:  B+
--------------------
Name:  Mike
Age:  32
Blood Group:  O-
--------------------
Name:  Anna
Age:  25
Blood Group:  AB+
--------------------
Name:  Tom
Age:  30
Blood Group:  A-
--------------------
Name:  Sara
Age:  27
Blood Group:  B-
--------------------
Name:  Paul
Age:  24
Blood Group:  O+
--------------------
Name:  Kate
Age:  29
Blood Group:  AB-
--------------------
Name:  Chris
Age:  26
Blood Group:  A+
--------------------
Name:  Nina
Age:  23
Blood Group:  B+
--------------------
'''
