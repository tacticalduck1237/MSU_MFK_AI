s = open('the_calls.txt')
c = s.readlines()
d = "/".join(c)
d = d.replace('\n', "")
d = d.split("/")
d = sorted(d, key=lambda w: (str(w.split("\t")[2]), -int( w.split("\t") [1])))
p='\n'.join(d)
fi=open('calls.txt',"a")
fi.writelines(p)
fi.close()
s.close()