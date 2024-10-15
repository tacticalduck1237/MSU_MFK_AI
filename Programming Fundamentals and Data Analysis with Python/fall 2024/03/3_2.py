s = open('input.txt')
c = s.read()
filtered_words = [word for word in c.split() if 'ё' in word]
d = '\n'.join(filtered_words)
print(d)
s.close()
