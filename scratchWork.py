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