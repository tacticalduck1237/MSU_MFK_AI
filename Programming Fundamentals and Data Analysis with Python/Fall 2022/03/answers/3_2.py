s = open('input.txt')
c = s.readlines()
b = ''.join(c)
a = b.split("\n")
stripped_lines= [line.strip() for line in a]
filtered_lines = [line for line in stripped_lines if 'ё' in line]
d = '\n'.join(filtered_lines)
print(d)
s.close()
