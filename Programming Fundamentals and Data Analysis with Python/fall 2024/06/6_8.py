result = {}
with open('input.txt') as file:
    for line in file:
        data = line.split()
        result.setdefault(data[1], []).append(data[0])
for key in sorted(result, key=len):
    print(f'{key}: {", ".join(sorted(result[key]))}')
