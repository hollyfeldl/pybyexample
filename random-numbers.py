# the pseudorandom number example
# https://gobyexample.com/random-numbers

import random
import time

def main():

	#Go defaults the seed with a constant of 1, Python detaults with the system time.
	#Both are bad for security uses.

	#Let's start with a constant to mimic Go

	random.seed(a=1)

	print("{0},{1}".format(random.randrange(0,100),random.randrange(0,100)))

	print(random.random())

	# compute a range of float random using math
	print("{0},{1}".format(
		(random.random()*5.0)+5.0, (random.random()*5.0)+5.0))

	# do the same using a uniform distibution
	print("{0},{1}".format(random.uniform(5.0,10.0),random.uniform(5.0,10.0)))

	# now explicity set the see from the current time -- would also happen if you pass None
	#(nano seconds not support until python 3.7)
	random.seed(a=time.time())
	print("{0},{1}".format(random.randrange(0,100),random.randrange(0,100)))

	random.seed(a=42)
	print("{0},{1}".format(random.randrange(0,100),random.randrange(0,100)))

	random.seed(a=42)
	print("{0},{1}".format(random.randrange(0,100),random.randrange(0,100)))
	

if __name__ == "__main__":
	main()

