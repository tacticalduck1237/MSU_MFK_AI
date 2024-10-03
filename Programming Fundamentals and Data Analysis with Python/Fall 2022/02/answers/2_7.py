letter = str(input())
shift = 1
s = ""
for l in letter:
    if l.isalpha():
        a = ord(l) + shift
        s += chr(a)
    else:
        s += l
print(s)
