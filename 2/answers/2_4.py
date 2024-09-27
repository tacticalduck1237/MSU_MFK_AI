s=str(input())
a=s.find('"')
b=s.rfind('"')
print(s[a+1:b])
