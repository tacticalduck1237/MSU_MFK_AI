s = open('input.txt')
c = s.read()
import string
punctuations = string.punctuation
c1=""
for char in c:
    if char not in punctuations:
        c1 += char
c1=c1.split()
filtered_words = [word for word in c1 if 'ё' in word]
d = '\n'.join(filtered_words)
print(d)
s.close()
