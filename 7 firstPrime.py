# 10001st prime

# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

def isPrime(num):						# works for all primes except 2...

	root = num ** (0.5)
	upper = int(math.ceil(root)) + 1
	count = 0

	for a in range(2,upper):
		if num % a == 0:
			count += 1
			break

	if count == 0: 
		return True
	else:
		return False

def findPrime(limit):
	count = 1 							# because isPrime(2) is False
	check = 2
	while count < limit:
		TF = isPrime(check)
		if TF is True:
			count += 1
			if count == limit:
				break
			check += 1
			print("TRUE, count = " + str(count) + ", check = " + str(check))
			print(" ")
		else:
			check += 1
			print("FALSE, count = " + str(count) + ", check = " + str(check))
			print(" ")
	return check 

print(findPrime(6))

