# the package example

from plus_pkg import plus_mod

def main():

	print("4+5 = {0}".format(plus_mod.Plus(4,5)))

	print("4+5+6 = {0}".format(plus_mod.PlusPlus(4,5,6)))

if __name__ == "__main__":
	main()

