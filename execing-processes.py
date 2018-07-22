# execing processes example
# https://gobyexample.com/execing-processes

import os

def main():

	binary = "ls"
	args = ["-a", "-l", "-h"]
	env = os.environ

	try:
		os.execvpe(binary, args, env)
	except:
		raise

if __name__ == "__main__":
	main()