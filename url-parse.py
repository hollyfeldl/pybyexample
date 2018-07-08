# URL parse example
# https://gobyexample.com/url-parsing

# Python 3 version
from urllib.parse import urlparse, parse_qs, parse_qsl
# Python 2.7
#from urlparse import urlparse, parse_qs, parse_qsl

def main():

	print("Using urllib.parse for Python 3 - For Python 2.7 consult urlparse")

	s = "postgres://user:pass@host.com:5432/path?k=v#f"


	# much of the syntax error checking happens when you pull the bits apart
	# do not worry about error checking
	u = urlparse(s)

	print(u)

	print(u.scheme)
	print(u.username)
	print(u.password)
	print(u.hostname)
	print(u.port)
	print(u.path)
	print(u.fragment)
	print(u.query)

	# python can parse the query into a list or a dict
	print(parse_qsl(u.query)) # just print the list

	m = parse_qs(u.query) # asign the dict to a var so we can work with it
	print(m)
	print(m["k"][0])


if __name__ == "__main__":
	main()