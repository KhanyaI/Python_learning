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

    return lst



if __name__ == '__main__':
    number_of_bits = 4
    bit_list_1 = flip(number_of_bits)









