num=int(input("Enter a num:"))
a=0
b=0
while num>0:
    a=num%10
    b=b*10+a
    num=num//10
print(f"Reverse order of the number:{b}")