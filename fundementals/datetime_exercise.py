import datetime
import pytz

date = datetime.date(2019, 8, 12)
print(date)

today = datetime.date.today()
print("Date is:", today)
print("Day is:", today.day)
print("Month is:", today.month)
print("Year is:", today.year)
print("Weekday is:", today.weekday())  # Monday is 0 -- Sunday  is 6
print("isoweekday is:", today.isoweekday())  # Monday is 1 -- Sunday is 7

t_delta = datetime.timedelta(days=7)
print("Today's date is:", today)
print("After a week from Today:", today + t_delta)
print("Before a week from Today:", today - t_delta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

b_day = datetime.date(2020, 8, 10)
till_bday = b_day - today
print("Day remains for B-day:", till_bday)
print("No of days remains for B-Day:", till_bday.days)
print("Total seconds remains for B-day:", till_bday.total_seconds())

time = datetime.time(9, 30, 45, 100000)
print("Time is:", time)
print("Hours:", time.hour)
print("Minutes:", time.minute)
print("Seconds:", time.second)
print("Microseconds:", time.microsecond)

date_time = datetime.datetime(2019, 8, 22, 12, 30, 45, 100000)
print("Current date & time:", date_time)

time_delta = datetime.timedelta(hours=12)
print("After 12 hours date & time:", date_time + time_delta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print("Date Time today:", dt_today)  # returns current local date time with a timezone none
print("Date Time now:", dt_now)  # gives option to pass a timezone
print("Date Time utcnow:", dt_utcnow)  # current utc time but tz info still set to none

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print("date time with pytz.UTC:", dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print("Date and Time utcnow() with pytz.UTC:", dt_utcnow)

# for tz in pytz.all_timezones:   # to see available time zones in python
#    print(tz)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
dt_mtn = dt_utcnow.astimezone(tz=pytz.timezone('US/Mountain'))
print(dt_mtn)

current_time = datetime.datetime.now()
print("Current Date Time is:", current_time)
print("Datetime to string:", current_time.strftime('%B %d,%Y'))

new_date = 'July 27, 2016'
print("String of date:", new_date)
final = datetime.datetime.strptime(new_date, '%B %d, %Y')
print("String to datetime:", final)

# difference between time delta
t1 = datetime.timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = datetime.timedelta(days=4, hours=11, minutes=4, seconds=54)
t3 = t1 - t2
print("Time delta 1:", t1)
print("Time delta 2:", t2)
print("t1 - t2=", t3)


local = datetime.datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))
tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
