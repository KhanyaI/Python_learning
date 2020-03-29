
def maxheap(A,heapify_size,i):
	l = 2*i+1
	r = 2*i+2
	largest = i
	if l < heapify_size and A[l] > A[largest]:
		largest= l
	if r < heapify_size and A[r] > A[largest]:
		largest = r
	if largest != i:
		A[i],A[largest] = A[largest],A[i]
		maxheap(A,heapify_size,largest)


def buildheap(A,build_size):
	for i in range (build_size//2,-1,-1):
		print(i)
		maxheap(A,build_size,i)



def heapsort(A):
	n = len(A)

	buildheap(A,n)
	while n > 0:
		A[0],A[n-1] = A[n-1],A[0]
		n = n-1
		maxheap(A,n,0)
	return A


array = [ 2, 11, 13, 5, 4, 7] 
heapsort(array)
print(array)

