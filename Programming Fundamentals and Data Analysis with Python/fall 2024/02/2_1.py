str1=input()
str1=str1.strip()
str2=input()
str2=str2.strip()
if str1==str2:
    print("A")
elif str1 in str2:
    print("B")
elif str2 in str1:
    print("C")
else:
    print("D")