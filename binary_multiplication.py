import time
import random

def binarymulti(a,b):
    temp1 = [] # initialize an empty list outside the for loop

    for i in range(0,len(a)): #for every digit in the array, doesn't matter which one
        temp2 = [] # initialize second list inside the for loop
        for j in range(0,len(b)): #for every
            product= a[i] * b[j]
            temp2.append(product)
        temp1.append(temp2)
        #print(temp2)
    print(temp1)

    sum = 0
    allproducts = []

    for i in range(0,len(a)):
        j = [0] * (len(a)-(i+1))
        final = temp1[i]+j
        # add modulus
        print(final)
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
    len_bit_lst = [2,4,8,10]
    for i in len_bit_lst[1:2]:

    	bit_list_1 = flip(i)
    	bit_list_2 = flip(i)
    	print(bit_list_1,bit_list_2)
    	binarymulti(bit_list_1,bit_list_2)









