

def Index(vs, t):
	for i in range(len(vs)):
		if vs[i] == t:
			return i
	return -1

def Include(vs, t):
	return Index(vs, t) >= 0


def main():

	strs = ["peach", "apple", "pear", "plum"]

	print(Index(strs, "pear"))
	print(Include(strs, "grape"))

if __name__ == "__main__":
    main()    



