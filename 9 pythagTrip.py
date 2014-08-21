# Special Pythagorean triplet

# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def isEven(n):
	if n % 2 == 0:
		return True
	else:
		return False

L = []

for a in range(1, 333):
	b1 = a + 1
	if isEven(a):
		b2 = (1000-a)/2 - 1
	else:
		b2 = (1000-a)/2
	subset = [a, b1, b2]
	L.append(subset)

for subset in L:
	a = subset[0]
	b1 = subset[1]
	b2 = subset[2]
	for b in range(b1, b2+1):
		A = a ** 2
		B = b ** 2
		C = (A + B)
		c = C ** (0.5)
		if a + b + c == 1000:
			print(a, b, c)
			d = a * b * c
			print(d)

