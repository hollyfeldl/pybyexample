# time formatting sample
# https://gobyexample.com/time-formatting-parsing

from datetime import date, time, datetime

# leverage python-dateutil for timezone and parsing stuffs
# https://pypi.org/project/python-dateutil/

from dateutil.parser import parse
from dateutil import tz



def main():

	t = datetime.now(tz.tzutc())
	t_pst = datetime.now(tz.gettz("America/Los_Angeles")) # for giggles do Pacific as well

	rfc3339_fmt = "%Y-%m-%dT%H:%M:%S%z" # not really because the time offset doesn't have colons

	print("This is not exactly RFC3339 -- time offset does not have colons")
	print(t.strftime(rfc3339_fmt))
	print(t_pst.strftime(rfc3339_fmt))

	print("There is a function to truncate this in 3.7 to seconds")
	print(t.isoformat()) # need to truncate to seconds
	# print(now.isoformat(timespec='seconds')) # Python3 version

	# Use the dateutil parser instead of datetime.strptime because of issues with timezone
	t1 = parse("2012-11-01T22:08:41+00:00")
	print(t1)

	print(datetime.strftime(t,"%I:%M%p"))
	print(datetime.strftime(t,"%a %b %m %H:%M:%S %Y"))
	print(datetime.strftime(t,"%Y-%m-%dT%H:%M:%S.%f%z"))

	t2 = parse("3 04 PM")
	print(t2)

	print("{0:d}-{1:02d}-{2:02d}T{3:02d}:{4:02d}:{5:02d}-00:00".
		format(t.year, t.month, t.day, t.hour, t.minute, t.second))


	try:
		t3_str = "2018-99-99"
		t3 = parse(t3_str)
	except ValueError as err:
		print("error parsing {0} is [{1}]".format(t3_str,err))


if __name__ == "__main__":
	main()
