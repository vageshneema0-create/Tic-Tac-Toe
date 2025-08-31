a=int(input("enter your 5-digit number:"))
b=a%10
print(b)
c=a//10
d=c%10
print(d)
e=c//10
f=e%10
print(f)
g=e//10
h=g%10
print(h)
i=g//10
j=i%10
print(j)
k=b*10000+d*1000+f*100+h*10+j
print(k)
l=str(k*5)
print("final answer is"+l+"!")

