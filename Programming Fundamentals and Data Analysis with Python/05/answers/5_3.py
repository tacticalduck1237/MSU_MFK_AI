s = open('med_research.txt')
c = s.readlines()
d = "/".join(c)
d = d.replace('\n', "")
d = d.split("/")
list_of_lists  = []
transposed=list()
for num in d:
    num = num.split()
    list_of_lists.append(num)
for i in range(len(list_of_lists[0])):
    row = list()
    for sublist in list_of_lists:
        row.append(sublist[i])
    transposed.append(row)
fi = open('output.txt', 'a')
for item in transposed:
    t = " ".join(item)
    fi.writelines(t + "\n")
fi.close()
s.close()
