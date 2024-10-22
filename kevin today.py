'''
python program to find temperature
author:kevin joseph
'''
tem=int(input("enter the temperature:"))
unit=input(" if temperature in celsius press 'C' or in fahrenheit press 'F':")
if unit=="C":
    f=(9/5*tem)+32
    print(tem,"celsius is",f,"fahrenheit")
elif unit=="F":
    c=5/9*(tem-32)
    print(tem,"fahrenheit is",c,"celsius")
else:
    print("enter the correct option:")


