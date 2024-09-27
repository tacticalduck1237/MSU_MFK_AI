from fractions import Fraction
a_inp = input()
b_inp = input()
c_inp = input()
a = Fraction(a_inp.replace(" ", "/"))
b = Fraction(b_inp.replace(" ", "/"))
c = Fraction(c_inp.replace(" ", "/"))
f = str(float(b/a +b/(a+c) - c/(c-a)))
n = f.find(".")
num = f[0:n+5]
last = int(f[n+5])
if last < 5:
	sol_1 = num
	print(sol_1)
else:
	x = num[n+4]
	last_s = str(int(x) + 1)
	num_1 = num[::-1]
	num_2 = num_1.replace(x, last_s, 1)
	sol_2 = num_2[::-1]
	print(sol_2)
