# line filters example
# https://gobyexample.com/line-filters
#
# expects a couple lines of text from a file piped in
#

import sys

def main():

	cnt = 0

	try:
		for l in sys.stdin:

			ucl = l.rstrip().upper()
			print("{0}".format(ucl))
			cnt = cnt + 1

	except:
		raise
	finally:
		print("Processed {0} lines.".format(cnt))


if __name__ == "__main__":
	main()