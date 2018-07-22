# the environmental var example
# https://gobyexample.com/environment-variables

import os

def main():

	# add new environment var
	os.environ["FOO"] = "1"

	# get a copy of it
	env = os.environ

	# try to get the keys
	try:
		print("FOO: {0}".format(env["FOO"]))
	except KeyError:
		print("FOO:")

	try:
		print("BAR: {0}".format(env["BAR"]))
	except KeyError:
		print("BAR:")

	print("")

	# dump out the variable names that are currently defined
	for pair in env:
		print("{0}".format(pair))

	print("************** ENV_VAR and Value *****************")

	# now dump the names and the values 
	for pair in env:
		print("{0}: {1}".format(pair, env[pair]))



if __name__ == "__main__":
	main()

