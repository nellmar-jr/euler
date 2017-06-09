#sieve of eratosthenes
def foo(n):
	A = [False] * 2 + [True] * (n - 1) #algoritmo de la sieve
	for i in range(int(n**0.5 + 1.5)): #https://en.wikipedia.org/wiki/Primality_test
		if A[i]:
			for j in range(i*i, n+1, i):
				A[j] = False
	return [i for i, prime in enumerate(A) if prime]
	#return [j for j, prime in enumerate(A) if prime]
		
k = 100

foo(k)
while (len(foo(k))) < 10001:
	k += 1
	print(len(foo(k)))
	foo(k)
print(foo(k))

#se puede mejorar computando previamente los 200 primeros primos
#y no permitir la comprobación con esos primos ya hallados