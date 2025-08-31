a=int(input())
b=int(input())
c=int(input())
even=(a%2==0 and b%2==0 and c%2==0)
if(even==True):
    if(a>b and c>b):
        print(b)
    elif(b>a and c>a):
        print(a)
    else:
        print(c)
else:
    if(a>b and a>c):
        if(a%2!=0):
            print(a)    
    elif(b>a and b>c):
        if(b%2!=0):
            print(b)
    else:
        print(c)       
