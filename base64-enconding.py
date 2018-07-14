# base64 encoding example
# https://gobyexample.com/base64-encoding

import base64

def main():

	data = "abc123!?$*&()'-=@~"

	sEnc = base64.standard_b64encode(data)
	print("Standard: {0}".format(sEnc))
	print("Decoded: {0}\n".format(base64.standard_b64decode(sEnc)))

	uEnc = base64.urlsafe_b64encode(data)
	print("URLSafe: {0}".format(uEnc))
	print("Decoded: {0}".format(base64.urlsafe_b64decode(uEnc)))

if __name__ == "__main__":
	main()