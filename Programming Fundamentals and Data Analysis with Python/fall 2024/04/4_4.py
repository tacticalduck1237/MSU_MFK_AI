s=open('input.txt')
a=s.readlines()
n=len(a)
i=0
minlist=[]
while i<n:
    b=a[i].strip()
    b=b.split(" ")
    i+=1
    minimal=float(min(b))
    minlist.append(minimal)
    maximum=max(minlist)
print(f"{maximum:.3f}")
s.close


#ИСПРАВЛЕННОЕ ЧАТГПТ
with open('input.txt') as s:
    lines = s.readlines()

min_list = []
for line in lines:
    # Strip and split each line into numbers
    numbers = line.strip().split(" ")
    # Convert each number to float and find the minimum in the line
    minimal = min(float(num) for num in numbers)
    min_list.append(minimal)

# Find the maximum of the minimum values
maximum = max(min_list)
print(f"{maximum:.3f}")
