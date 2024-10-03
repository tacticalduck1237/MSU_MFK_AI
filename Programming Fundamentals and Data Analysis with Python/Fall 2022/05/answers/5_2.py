s = open('poe_unpublished.txt')
c = s.readlines()
d = "/".join(c)
d = d.replace('\n', "")
d = d.split("/")
list_1 = []
for words in d:
    words = words.split()
    words.sort(key=len)
    list_1.append(words)
list_1 = sorted(list_1, key=len)
fi = open('poe_decode_attempt.txt', 'a')
for stings in list_1:
    t=" ".join(stings)
    fi.writelines(t+ "\n")
fi.close()
s.close()
