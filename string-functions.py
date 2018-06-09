# the string functions example
# https://gobyexample.com/string-functions

def main():

	# to get contains -- wrap find with in-line if-then
	print("Contains:  {}".format(True if "test".find("es") > -1 else False))

	print("Count:     {}".format("test".count("t")))
	print("HasPrefix: {}".format("test".startswith("te")))
	print("HasSuffix: {}".format("test".endswith("st")))
	print("Index:     {}".format("test".index("e")))
	print("Join:      {}".format("-".join(["a","b"])))
	print("Repeat:    {}".format("a" * 5))
	print("Replace (n){}".format("foo".replace("o","0",-1)))
	print("Replace    {}".format("foo".replace("o","0",1)))
	print("Split      {}".format("a-b-c-d-e".split("-")))
	print("ToLower    {}".format("TEST".lower()))
	print("ToUpper    {}".format("test".upper()))
	print("")
	print("len: {}".format(len("hello")))
	print("char:{}".format(ord("hello"[1])))


if __name__ == "__main__":
	main()