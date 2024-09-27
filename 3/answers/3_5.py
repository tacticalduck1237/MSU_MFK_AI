import itertools as it
s = open('studygroup.txt')
c = s.read()
d=c.split(" ")
for x, y, z in it.combinations(d, 3):
    print('1:', x,'2:', y,'3:', z, sep=' ', end='\n')
s.close()
