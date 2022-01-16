def repeated(x):
	repeat = []
	for i in range(len(x)):
		for j in range(i+1,len(x)):
			if x[i] == x[j] and x[i] not in repeat:
				repeat.append(x[i])
	return print_list(repeat)
def print_list(x):
	for num in x:
		print(num,end=" ")

lst = ['1','2','2','4','1','3','3','7']
repeated(lst)

