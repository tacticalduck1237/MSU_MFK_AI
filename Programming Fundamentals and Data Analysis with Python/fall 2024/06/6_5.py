s = open('input.txt')
c = s.readlines()
d = "/".join(c)
d = d.replace('\n', "")
d = d.split("/")
animals = set()
list_1 = []
for words in d:
    words = words.split()
    list_1.append(words)
for an in list_1:
    f = an[1]
    animals.add(f)
animals = sorted(animals, key=len)
print(*animals, sep='\n')
s.close()
