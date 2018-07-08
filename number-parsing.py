#number parsing example
# https://gobyexample.com/number-parsing

def main():

	print(float("1.234"))

	print("{0},{1}".format(int("-123"),int("123")))

	# int() can be used with other bases -- if provided a string, specify explicitly
	print("{0},{1}".format(int("0x1c8", 16),int(0x1c8)))

	print("Python int type is signed and unlimited percision -- unsigned does not apply.")

	try:
		print(int("wat"))
	except ValueError as err:
		print("Parsing Problem Example -- ValueError [{0}].".format(err))

if __name__ == "__main__":
	main()