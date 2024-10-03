s=open('input.txt')
c = s.read()
d=c.split(" ")
amount =float(d[0])
period=float(d[1])
rate =float(d[2])
period=period*12
amount1=amount
i=1
f=open('output.csv', 'a')
print("Месяц", "Сумма на вкладе", "Начисление", sep=",", file=f)
while i<=period:
    amount2 = amount1
    amount1=amount*(1+(rate/12/100))**i
    gain=amount1-amount2
    print(f"{i},{amount1:0.2f},{gain:0.2f}", sep=",", file=f)
    i+=1
s.close()
f.close()
