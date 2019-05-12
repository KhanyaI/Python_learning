def buildheap


def maxheap(A,i):
	l = A[i]-1
	r = A[i]+1




def heapsort(A):
	buildheap(A)
	for i in range(len(A),2,-1):
		A[1],A[i] = A[i],A[1]
		#reduce heap size
		maxheap(A,1)
#trying
