# switch example

import calendar
from datetime import datetime

def caseFunc(x):
    return{
        1 : "one",
        2 : "two",
        3 : "three"
    }.get(x, "undefined") # undefined is the default


def main():

    # Python does not have a case/switch structure
    # first replacement for switch -- dictionary where
    # the cases are the dictionary keys

    i = 2
    print("Write", i, "as", caseFunc(i))

    # use in a list in place of multiple cases
    if datetime.today().weekday() in [calendar.SATURDAY, calendar.SUNDAY]:
        print("It's the weekend")
    else:
        print("IT's the weekday")

    # the Go example reduces to an if-else
    if datetime.now().hour < 12:
        print("It's before noon")
    else:
        print("It's after noon")

    # punt on interfaces for now

main()

