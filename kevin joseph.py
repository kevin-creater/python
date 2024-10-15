'''
python program to find sum of digits of number
author:kevin joseph
'''
num=int(input("enter a number:"))
sum=0
while(num>0):
     r=num%10
     num=num//10
     sum=sum+r
print(sum)





