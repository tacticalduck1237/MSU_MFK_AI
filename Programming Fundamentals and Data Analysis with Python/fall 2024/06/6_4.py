from collections import Counter
def least_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(-1)[0][0]
List=list(input())
print(least_frequent(List))