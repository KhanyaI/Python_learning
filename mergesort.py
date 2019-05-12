def mergesort(l,r):
    result=[]
    i = j = 0
    while i <len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i = i+1
        else:
            result.append(r[j])
            j = j+1
    result += l[i:]
    result += r[j:]
    return result


def merge(lst):
    if (len(lst) == 0 or len(lst)==1):
        return lst
    mid = len(lst)//2
    l = merge(lst[:mid])
    r = merge(lst[mid:])
    return mergesort(l,r)


lst=[3,2,4,1,9,5]
print(msort(lst))
