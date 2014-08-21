# Multiples of 3 and 5

# Problem 1

# If we list all the natural numbers below 10 that are multiples 
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def checkNum(a):
	if a % 3 == 0 or a % 5 == 0:
		return a
	else:
		return 0

def addMultiples(x):
	answer = 0
	for num in range(0, x):
		check = checkNum(num)
		answer += check
	return answer

