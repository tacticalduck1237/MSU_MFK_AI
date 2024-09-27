def bin_search(lst):
    val=1415
    first = 0
    last = len(lst)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if int(lst[mid]) == val:
            index = mid
        else:
            if val<int(lst[mid]):
                last = mid -1
            else:
                first = mid +1
    return index
