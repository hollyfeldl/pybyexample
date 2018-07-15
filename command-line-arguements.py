# Command Line Arguements Example
# https://gobyexample.com/command-line-arguments

import argparse

def main():

	p = argparse.ArgumentParser(description="Command Line Example")
	p.add_argument("strings", metavar="s", type=str, nargs="+")

	args = p.parse_args()

	argsWithProg = [p.prog]
	argsWithProg.extend(list(args.strings))
	argsWithoutProg = list(args.strings) # make a copy of the arg list
	arg = args.strings[2]

	print("{0}".format(argsWithProg))
	print("{0}".format(argsWithoutProg))
	print("{0}".format(arg))


if __name__ == "__main__":
	main()