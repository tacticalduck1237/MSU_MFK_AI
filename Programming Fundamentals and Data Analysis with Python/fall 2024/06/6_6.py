s = open('input.txt')
c = s.readlines()
d = "/".join(c)
d = d.replace('\n', "")
d = d.split("/")
animals = set()
animals2 = set()
animals1 = set()
list_1 = []
for words in d:
    words = words.split()
    list_1.append(words)
for an in list_1:
    if an[2]=='male':
        f = an[1]
        animals1.add(f)
    if an[2]=='female':
        f = an[1]
        animals2.add(f)
animals=animals1.intersection(animals2)
if animals!=set():
    animals = sorted(animals, key=len)
    print(*animals, sep='\n')
else:
    print('0')
s.close()
