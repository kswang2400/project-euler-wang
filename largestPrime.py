# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def isPrime(n):
	root = n ** (0.5)
	upper = int(math.ceil(root))
	count = 0
	for a in range(2,upper):
		if n % a == 0:
			count += 1
	if count == 0: 
		return True
	else:
		return False

def listFactors(n):
	lista = []
	listb = []
	root = n ** (0.5)
	upper = int(math.ceil(root))
	for a in range(2, upper):
		if n % a == 0:
			b = n / a
			lista.append(a)
			listb.append(b)
	answer = lista + listb[::-1]
	# print(answer)
	return answer

L = listFactors(600851475143)
answer = []
for num in L:
	check = isPrime(num)
	if check is True:
		answer.append(num)
# print(answer)
print(answer[-1])
