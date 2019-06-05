#Naive Matrix Multiplication

def mm(A,B):
	C= [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	rows_A = len(A)
	cols_A = len(A[0])
	cols_B = len(B[0])
	for i in range(rows_A):
		for j in range(cols_B):
			for k in range(cols_A):
				C[i][j] = C[i][j] + (A[i][k] * B[k][j])

	return C


A = [[10,0,3,8],[51,20,1,4],[7,25,46,74],[2,9,52,63]]
B = [[11,2,8,4],[15,2,31,45],[17,24,6,44],[21,39,42,53]]
print(mm(A,B))

