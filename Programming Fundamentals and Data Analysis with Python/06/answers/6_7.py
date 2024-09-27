from collections import Counter
def most_frequent(List):
	occurence_count = Counter(List)
	return occurence_count.most_common(1)[0][0]
s = open('input.txt')
c = s.readlines()
d = "/".join(c)
d = d.replace('\n', "")
d = d.split("/")
animals = list()
list_1 = []
for words in d:
	words = words.split()
	list_1.append(words)
for an in list_1:
	f = an[1]
	animals.append(f)
List = animals
count = (Counter(List))
animal = list(count.keys())
value = list(count.values())
value = str(value)
value = value.replace("[", "")
value = value.replace("]", "")
value = value.replace(",", "")
value = value.split(' ')
zipped_animals = list(zip(animal, value))
zip_an = []
for t in zipped_animals:
	t = " - ".join(t)
	zip_an.append(t)
zip_an = sorted(zip_an, key=lambda w: int(w.split()[-1]), reverse=True)
print(*zip_an, sep="\n")
s.close()
