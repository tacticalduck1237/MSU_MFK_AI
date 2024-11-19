from collections import Counter

def least_frequent(List):
    occurrence_count = Counter(List)
    # Sort by frequency, then by number
    least_common = sorted(occurrence_count.items(), key=lambda x: (x[1], x[0]))[0]
    return least_common[0]

# Read input and convert it into a list of integers
List = list(map(int, input()))
print(least_frequent(List))
