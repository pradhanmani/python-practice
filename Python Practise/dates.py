import datetime
import pytz

dt_nepal = datetime.datetime.now(tz=pytz.timezone('Asia/Kathmandu'))
print(dt_nepal.strftime('%B %d, %Y'))

dt_str = 'June 09, 2026'

dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt)
# strftime - Datetime to String
# strptime - String to Datetime

# for tz in pytz.all_timezones:
#     print(tz)
