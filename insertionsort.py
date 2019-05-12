#take unsorted list and sort it
def tosort(list1):
	i = 1
	while  i < len(list1):
		x = list1[i]
		j = i-1
		while j >= 0 and list1[j] > x:
			list1[j+1] = list1[j]
			j = j-1
		list1[j+1] = x
		i = i +1
		print(list1)
	return list1
list1 = [6,3,10,1]
#sorted_list = tosort(list1)
print(tosort(list1),len(list1))





