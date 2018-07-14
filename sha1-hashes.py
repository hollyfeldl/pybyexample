# hashing examples
# https://gobyexample.com/sha1-hashes

import hashlib


def main():

	s = "sha1 this string"

	h = hashlib.sha1()
	h.update(s)

	print(s)
	print("sha1: {0}".format(h.hexdigest()))

	h_sha256 = hashlib.sha256()
	h_sha256.update(s)

	print("sha256: {0}".format(h_sha256.hexdigest()))

	h_sha512 = hashlib.sha512()
	h_sha512.update(s)

	print("sha512: {0}".format(h_sha512.hexdigest()))

if __name__ == "__main__":
	main()

