""""

def binarymulti(a,b):
	#array1 = [int(x) for x in str(a)]
	#array2 = [int(x) for x in str(b)]
	count = 0
	sum_total = 0

	while count < b:
		sum_total = sum_total+a
		count = count+1
		print(sum_total)
	return sum_total
		

if __name__ == '__main__':
	bin1 = 1001
	bin2 = 1010
	binarymulti(bin1,bin2)
"""
import time
import random
import matplotlib.pyplot as plt



def binarymulti(a,b):
	#array1 = [int(x) for x in str(a)] #Taking the binary number as a string, then breaking it down into individual digits and return them as integers in an array
	#array2 = [int(x) for x in str(b)]

	temp1 = [] # initialize an empty list outside the for loop

	for i in range(0,len(a)): #for every digit in the array, doesn't matter which one
		temp2 = [] # initialize second list inside the for loop
		for j in range(0,len(b)): #for every 
			product= a[i] * b[j]
			temp2.append(product)
			#print (array1[i], array2[j], product)
		temp1.append(temp2)
	#print(temp1)

	sum = 0
	allproducts = []

	for i in range(0,len(a)):
		j = [0] * i
		final = temp1[i]+j
		#print(final)
		num = int("".join(map(str, final)))
		#print(num)
		sum = sum + num
	
	print('The product of these two binary numbers is:', sum) 

def flip(n):
	lst = []
	i= 0
	while i < n:
		flip = random.randint(0, 1)
		lst.append(flip)
		i = i+1
	#print (lst)
	#number = int("".join(map(str, lst)))



if __name__ == '__main__':
	def generate(n):
		lst = []
		i= 0
		while i < n:
			flip = random.randint(0, 1)
			lst.append(flip)
			i = i+1
	x = lst
	print(x)
	#binarymulti(x,y)



"""if __name__ == "__main__":
	timelist=[]
	numbers=[]

	for i in range(0,10): ## Do for increasing sizes of bit, 2 bits, 3 bits. input them as tuples

		start = time.clock()

		a = random.randint(0, 5000)
		b = random.randint(0, 5000)
		bin1 = 
		bin2 = format(b,'08b')
		numbers.append([bin1,bin2])
		binarymulti(bin1,bin2)
		end = time.clock()
		final = end - start
		timelist.append(final)
	#print(timelist,numbers)



"""
"""
X = numbers
y = timelist
plt.plot(X,y)
plt.show() """





	



	