# command line flages examples
# https://gobyexample.com/command-line-flags

import argparse

def main():

	p = argparse.ArgumentParser(description=
		"""Command Line Flag Example --
		Python argparse does not use '=' for arguement assignment..."""
		)
	p.add_argument("--word", default="foo", type=str, nargs="?", help="a string")
	p.add_argument("--numb", default=42, type=int, nargs="?", help="an int")
	p.add_argument("-f", "--fork", action="store_true", help="a bool")
	p.add_argument("--svar", default="bar", type=str, nargs="?", help="a string")
	p.add_argument("tail", help="the remaining arguments", nargs=argparse.REMAINDER)

	flags = p.parse_args()

	print("word: {0}".format(flags.word))
	print("numb: {0}".format(flags.numb))
	print("fork: {0}".format(flags.fork))
	print("svar: {0}".format(flags.svar))
	print("tail: {0}".format(flags.tail))


if __name__ == "__main__":
	main()