# the collection functions example
# https://gobyexample.com/collection-functions


def Index(vs, t):
	for i in range(len(vs)):
		if vs[i] == t:
			return i
	return -1

def Include(vs, t):
	return Index(vs, t) >= 0


def GoAny(vs, f):
	for i in vs:
		if f(i):
			return True
	return False

def GoAll(vs, f):
	for i in vs:
		if not f(i):
			return False
	return True

def Filter(vs, f):
	vsf = []
	for i in vs:
		if f(i):
			vsf.append(i)
	return vsf

def GoMap(vs, f):
	vsm = []
	for v in vs:
		vsm.append(f(v))
	return vsm

def main():

	strs = ["peach", "apple", "pear", "plum"]

	print(Index(strs, "pear"))
	print(Include(strs, "grape"))

	print(GoAny(strs, lambda x: x.startswith('p')))
	print(GoAll(strs, lambda x: x.startswith('p')))
	print(Filter(strs, lambda x: False if x.find('e') < 0 else True ))
	print(GoMap(strs, lambda x: x.upper()))

if __name__ == "__main__":
    main()    



