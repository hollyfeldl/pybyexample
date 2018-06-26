# time example
# https://gobyexample.com/time

from datetime import date, time, datetime, timedelta
import calendar

# leverage pytz for timezone stuffs
# https://pypi.org/project/pytz/
from pytz import timezone
import pytz


def main():

	now = datetime.now(pytz.utc)

	# setup a format string for the time output
	fmt = '%Y-%m-%d %H:%M:%S %Z%z'
	print(now.strftime(fmt))

	# print the datetime in the pacific timezone
	pacific = pytz.timezone("US/Pacific")
	print(datetime.now(pacific))

	# Python only goes to milliseconds, Go goes to nanoseconds
	# Python time zones are defined by UTC offset instead of location like Go

	then = datetime.combine(date(2009, 11, 17) , time(20, 34, 58, 651387, pytz.utc))
	print(then.strftime(fmt))

	print(then.year)
	print(then.month)
	print(then.day)
	print(then.hour)
	print(then.minute)
	print(then.second)
	print(then.microsecond)
	print(then.tzinfo)

	print(calendar.day_name[then.weekday()])

	# do some date comparisions 
	print(True if then < now else False)
	print(True if now < then else False)
	print(True if then == now else False)

	# do some date math
	diff = now - then

	print(diff)
	print(diff.total_seconds()/3600.0)
	print(diff.total_seconds()/60.0)
	print(diff.total_seconds())
	print(diff.total_seconds()*1000000.0)

	print(then + diff)
	print(then - diff)


if __name__ == "__main__":
	main()