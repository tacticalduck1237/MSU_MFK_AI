count = 0
total_sum = 0

while True:
    number = int(input())
    if number == 0:
        break

    binary_representation = bin(number)[2:]
    zero_count = binary_representation.count('0')

    if zero_count == 3:
        count += 1
        total_sum += number

print(count, total_sum)