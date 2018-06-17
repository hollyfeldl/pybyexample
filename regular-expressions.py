# the regular expressions example
# https://gobyexample.com/regular-expressions

def main():

	import re

	# use re.match directly -- note using raw string notation
	# see https://docs.python.org/3/library/re.html
	print( True if re.match(r"p[a-z]+ch", "peach") else False ) # a match object will be true if success

	# compile a rule
	r = re.compile(r"p[a-z]+ch")

	print( True if r.match("peach") else False )
	print(r.match("peach punch").group())
	print(r.match("peach punch").span())

	# unable to find submatch functions
	print("Skip submatch example -- need to look for functionality")

	print(r.findall("peach punch pinch"))
	# print the indexes of the findings
	r_list = []
	for m in r.finditer("peach punch pinch"):
		r_list.append(m.span())
	print(r_list)

	print("Skip the byte examples and the must compile examples")

	print(r.sub("<fruit>","a peach"))

	# use a lambda to return the upper of the result of the search
	print(r.sub( lambda x: x.group().upper(), "a peach"))

if __name__ == "__main__":
	main()