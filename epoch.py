# the epoch example
# https://gobyexample.com/epoch

import time

def main():

	secs = time.time()
	now = time.ctime(secs)

	print("NOTE: time.time_ns() is not supported until Python 3.7")
	nanos = secs * 1000 * 1000000  # mock it for now

	millis = nanos / 1000000

	print(now)
	print(secs)
	print(millis)
	print(nanos)

if __name__ == "__main__":
	main()