# reading files example
# https://gobyexample.com/reading-files
#
# expecting a file /tmp/dat
# $ echo "hello" > /tmp/dat
# $ echo "go" >> /tmp/dat
#

import io


def main():

	# error handling with files is usually handled in a try block
	try:
		fn = io.open("/tmp/dat", mode="r")
		dat = fn.read()
		print(dat)
	except:
		raise
	finally:
		fn.close()

	
	try:
		# re-open the file in binary mode
		f = io.open("/tmp/dat", mode="rb")

		# read five bytes
		n1 = f.read(5)
		print("{0:d} bytes: {1}".format(len(n1),n1))

		# seek the sixth position and read two bytes
		f.seek(6)
		o2 = f.tell()
		n2 = f.read(2)
		print("{0:d} bytes @ {1:d}: {2}".format(len(n2),o2,n2))

		# read in one effort
		f.seek(6)
		o3 = f.tell()
		n3 = f.read1(2)
		print("{0:d} bytes @ {1:d}: {2}".format(len(n3),o3,n3))

		# rewind
		f.seek(0)

	except:
		raise
	finally:
		f.close()


	try:
		# re-open with explicit buffering
		fb = io.open("/tmp/dat", mode="rb", buffering=4)

		# look ahead at most one read (so constrained by four bytes)
		b4 = fb.peek(5)
		print("5 bytes: {0}".format(b4))

	except:
		raise
	finally:
		fb.close()


if __name__ == "__main__":
	main()