from collections import Counter
def least_frequent(List):
    occurrence_count = Counter(List)
    # Get all elements sorted by frequency (ascending order) and pick the first
    least_common = occurrence_count.most_common()[-1]
    return least_common[0]
List=list(input())
print(least_frequent(List))