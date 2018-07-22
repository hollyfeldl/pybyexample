# the spawning processes example
# https://gobyexample.com/spawning-processes

import subprocess

def main():

	try:
		out = subprocess.check_output(["date"])
	except:
		raise

	print("> date")
	print(out)


	grepCmdString = "grep hello"
	try:
		grepCmd = subprocess.Popen(grepCmdString, 
			shell=True, stdin=subprocess.PIPE, 
			stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		grepOut = grepCmd.communicate(b"hello grep\ngoodbye grep")

	except:
		raise

	if grepOut[1] == "":
		print("> {0}".format(grepCmdString))
		print("{0}".format(grepOut[0]))
	else:
		print("Command generated error...")
		print("{0}".format(grepOut[1]))

	lsCmdString = "bash -c 'ls -a -l -h'"
	try:
		lsCmd = subprocess.Popen(lsCmdString,
			shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		lsOut = lsCmd.communicate()
	except:
		raise

	if lsOut[1] == "":
		print("> {0}".format(lsCmdString))
		print("{0}".format(lsOut[0]))
	else:
		print("Command generated error...")
		print("{0}".format(lsOut[1]))		

if __name__ == "__main__":
	main()