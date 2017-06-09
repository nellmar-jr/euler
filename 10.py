#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
n = 2000000
def foo(n):
	A = [False] * 2 + [True] * (n - 1)
	for i in range(int(n**0.5 + 1.5)):
		if A[i]:
			for j in range(i*i, n+1, i):
				A[j] = False
	return [i for i, pr in enumerate(A) if pr]
	
print(sum(foo(n)))