import itertools

for p in itertools.product("012", repeat=3):
	print("".join(p))

for p in itertools.permutations("012", 3):
	print("".join(str(x) for x in p))

for p in itertools.combinations("012", 3):
	print("".join(p))
