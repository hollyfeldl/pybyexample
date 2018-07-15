# writing files example
# https://gobyexample.com/writing-files

import io

def main():

	# write only works with unicode strings
	d1 = u"hello\ngo\n"

	# write a string
	try:
		fn = io.open("/tmp/dat1", mode="wt")
		fn.write(d1)

	except:
		raise
	finally:
		fn.close()

	# now write some binary stuff -- oh and do it buffering
	try:
		f = io.open("/tmp/dat2", mode="wb", buffering=64)

		d2 = bytearray([115, 111, 109, 101, 10])
		n2 = f.write(d2)
		print("wrote {0} bytes".format(n2))

		n3 = f.write(u"writes\n")
		print("wrote {0} bytes".format(n3))

		f.flush() # there is no sync

		n4 = f.write(u"buffered\n")
		print("wrote {0} bytes".format(n4))

	except:
		raise
	finally:
		f.flush() # flush the buffers before we close
		f.close()


if __name__ == "__main__":
	main()
