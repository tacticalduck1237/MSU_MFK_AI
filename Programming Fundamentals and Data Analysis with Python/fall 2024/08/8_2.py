import numpy
s = open('input.txt')
c = s.read()
c=c.replace('\n', "")
d = c.split(" ")
e=[eval(i) for i in d]
print("{:.2f}".format(numpy.median(e)), "{:.2f}".format(numpy.mean(e)), "{:.2f}".format(numpy.std(e)), sep=" ")
s.close()
