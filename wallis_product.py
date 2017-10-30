product = 1
for k in range(1, 8500):
	term_k = 4 * k * k / ((2 * k - 1) * (2 * k + 1))
	product = product * term_k
	if (product * 2 >= 3.1415):
		print (k)
		print (product * 2)
		break
	#print ("----------")
	#print (product * 2)