# the JSON example
# https://gobyexample.com/json

import json

class response1:
    def __init__(self, page=None, fruits=[]):
        self.page = page
        self.fruits = fruits
    def __repr__(self):
        # put the struct into a dict
        theRepr={}
        theRepr["page"] = self.page
        theRepr["fruits"] = self.fruits
        return str(theRepr)


def main():

	print(json.dumps(bool(True)))
	print(json.dumps(int(1)))
	print(json.dumps(float(2.34)))
	print(json.dumps(str("gopher")))

	slcD = ["apple", "peach", "pear"]
	print(json.dumps(slcD))

	mapD = {"apple": 5, "lettuce": 7}
	print(json.dumps(mapD))

	#res1D = response1(page=1, fruits=["apple", "peach", "pear"])
	#print(json.dumps(res1D))
	#get TypeError: Object of type 'response1' is not JSON serializable
	print("skip the encoding of custom classes for now")


	byt = '{"num":6.13,"strs":["a","b"]}'
	dat = json.loads(byt)

	print(dat)

	print(float(dat["num"]))

	print(str(dat["strs"][0]))

	print("skip the custom decoding of JSON classes")

if __name__ == "__main__":
	main()
