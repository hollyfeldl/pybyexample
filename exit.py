# exit example
# https://gobyexample.com/exit
# to test use 
# > python exit.py; echo $?

import sys

def main():

	sys.exit(3)

	print("!")

if __name__ == "__main__":
	main()