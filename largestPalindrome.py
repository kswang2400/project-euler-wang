# Largest palindrome product

# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2 digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def checkPal(n):
	a = str(n)
	b = str(n)[::-1]
	if a == b:
		return True
	else:
		return False

L = []

for n in range(100, 1000):
	for a in range(100,1000):
		b = n * a
		c = checkPal(b)
		if c is True:
			L.append(b)
			break

print(L)
m = max(L)
print(m)
