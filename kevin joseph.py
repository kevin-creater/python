'''
python program to determine the smallest of three numbers
'''
num_1=int(input("enter the first number:"))
num_2=int(input("enter the second number:"))
num_3=int(input("enter the third number:"))
if num_1<num_2 and num_3:
     print("smallest:",num_1)
elif num_2<num_1 and num_2<num_3:
     print ("smallest:",num_2)
else:
     print(num_3)





