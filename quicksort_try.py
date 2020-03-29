def partition(A,p,r):
	pivot = A[r]
	i  = p-1
	for j in range(p,r):
		if A[j] <= pivot:
			i = i+1
			A[i],A[j] = A[j],A[i]
	A[i+1],A[r] = A[r],A[i+1]
	return(i+1)



def quicksort(A,p,r):
	if p < r:
		k = partition(A,p,r)
		return quicksort(A,p,k-1)
		return quicksort(A,k+1,r)


array = [35,43,12,66,3,8]
last = len(array)
quicksort(array,0,last-1)
print(array)

