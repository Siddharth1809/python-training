import datetime
from dateutil.relativedelta import *  # pip install python--dateutil
from dateutil.parser import *
from dateutil.tz import *
from dateutil.rrule import *

# relativedelta examples
Now = datetime.datetime.now()
Today = datetime.datetime.today()
print("Current date time:", Now)
result = Now + relativedelta(months=+1, weeks=+1, hour=10)  # next month plus one week at 10 am
print("next month plus one week at 10 am:", result)

result_1 = Now + relativedelta(years=+1, months=-1)  # one month before one year
print("one month before one year:", result_1)

result_2 = datetime.date(2019, 8, 20) + relativedelta(months=+1)
print("One month after 2019-08-20:", result_2)

print("Next Friday:", Today + relativedelta(weekday=FR))

print("Last Friday in this month:", Today + relativedelta(days=+11, weekday=FR(-1)))

print("Next Tuesday but not today:", Today + relativedelta(days=+1, weekday=TU))

my_bday = datetime.datetime(1998, 8, 10)
print("Current date time:", Now)
print("How old am I:", relativedelta(Now, my_bday))
print("Today:", Today)
print("How old am I:", relativedelta(Today, my_bday))

# parse examples
print(parse("Tue Aug 20 10:36:28 2019"))

# ISO format
print(parse("2019-08-20T10:49:41.5-03:00"))

print(parse("20190820"))

print(parse("Tue Aug 20 10am 2019"))
print(parse("Tue Aug 20 10pm 2019"))

print(parse("20th of August 2019"))

s = "Today is 25 of August of 2019, exactly at 12:11:41 with timezone -03:00."
print(parse(s, fuzzy=True))

print(parse("10h36m28.5s"))

print(parse("20-08-2019", dayfirst=True))
print(parse("20-08-19", yearfirst=True))

print(parse("Tue Aug 20 12:12:12 US 2003", ignoretz=True))

# rrule examples
# every 10 days 5 occurrences
print(list(rrule(DAILY, interval=10, count=5, dtstart=parse("20190820"))))

# everyday in january for 3 years
print(list(rrule(YEARLY, bymonth=1, byweekday=range(7), dtstart=parse("20190820"), until=parse("20220820"))))
