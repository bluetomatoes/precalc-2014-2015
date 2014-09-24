def pascal(n):
	line = [1]
	for k in range(n):
		line.append(line[k] * (n-k) / (k+1))
	return line

def ecalculate(e):
	count = 0
	for k in range(e+1):
		count  = count + float(pascal(e)[k])/e**k
	return count
i= 0
while i < 100:
	print i, ecalculate(i), 2.718281828459045235360-ecalculate(i)
	i+=1
