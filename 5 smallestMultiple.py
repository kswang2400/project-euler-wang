# Smallest multiple

# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?

L = range(2,21)
print(L)

F = 1

for num in L:
	if num == 1:
		break
	else:
		F = num * F
		for ind, key in enumerate(L):
			if key % num == 0:
				F = F * num
				L[ind] = key / num
				print(L)
				break

