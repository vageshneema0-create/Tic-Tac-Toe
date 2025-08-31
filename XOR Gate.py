x=bool(input())
y=bool(input())
m=(x and (not y)) or ((not x) and y)
print(m)