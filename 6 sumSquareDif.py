# Sum square difference

# Problem 6

# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.

def sumSquares(n):
	count = 0
	for nums in range(1, n+1):
		square = nums ** 2
		count += square
	print(count)
	return count

sumSquares(10)
a = sumSquares(100)

def squareSums(n):
	count = 0
	for nums in range(1, n+1):
		count += nums
	ans = count ** 2
	print(ans)
	return ans

squareSums(10)
b = squareSums(100)

print(b-a)

