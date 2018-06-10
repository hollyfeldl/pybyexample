# the string formatting example
# https://gobyexample.com/string-formatting

import base64
import sys

class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        # make the representation look like Go structs with fields
        return ("{{x:{0} y:{1}}}".format(repr(self.x), repr(self.y)))
    def __str__(self):
        # make the string look like Go structs string representation
        return ("{{{0} {1}}}".format(repr(self.x), repr(self.y)))

def main():

	p = point(1,2)
	print("{0!s}".format(p)) # the value
	print("{0!r}".format(p)) # the value with the field names (based on the construction of the class
	print("{0}{1!r}".format(p.__class__, p))
	print(p.__class__)

	print("{0}".format(True)) 							# no special formatting for booleans
	print("{0:d}".format(123)) 							# number formatting (no diff between int and dec)
	print("{0:b}".format(14))							# binary formatting
	print("{0}".format(chr(33)))						# return the character associated with the number (unicode)
	print("{0:x}".format(456))							# return hex (lowercase)
	print("{0:f}".format(78.9))							# number formatting using f vs d has a default of 6 decimals
	print("{0:.1f}".format(78.9))						# number formatting using f with magnitude
	print("{0:e}".format(123400000.0))					# scientific -- lowercase
	print("{0:E}".format(123400000.0))					# scientific -- uppercase
	print("{0:s}".format('"string"'))					# strings

	try:
		print("{0:s}".format(base64.b16encode("hex this")))	# return the hex of this
	except TypeError as err:
		print("Example not V3 safe -- {0}".format(err))

	print("Skip pointers")
	print("|{0:6d}|{1:6d}|".format(12,345))				# fixed width numbers
	print("|{0:6.2f}|{1:6.2f}|".format(1.2,3.45))		# fixed width decimals
	print("|{0:<6.2f}|{1:<6.2f}|".format(1.2,3.45))		# fixed width decimals -- left justified
	print("|{0:>6s}|{1:>6s}|".format("foo","b"))		# fixed width strings -- right justified
	print("|{0:6s}|{1:6s}|".format("foo","b"))			# fixed width strings -- left justified is default

	sys.stdout.write("a {0}\n".format("string"))		# format applied to the string not the output method
	sys.stdout.flush()							

	try:
		assert 1 + 1 == 3 , "an {0}".format("error")	# formatting is applied to the error not the method
	except AssertionError as err:
		print(err)


if __name__ == "__main__":
	main()