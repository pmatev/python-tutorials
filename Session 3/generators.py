
def alphabet(n):
	for i in range(n):
		yield alpha[i]

gen = alphabet(2)
next(gen)
next(gen)
next(gen)

gen2 = alphabet(2)
