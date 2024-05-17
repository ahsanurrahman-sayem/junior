from datetime import datetime,timedelta
from pytz import utc



def today():
	return str(date.today())

def currentTime():
	return datetime.now()

def now():
	return datetime.now(utc).strftime("%H:%M:%S %p %Z %A %d, %B %Y")


def getutc(offset_hours):
    # Get the current UTC time
	return (datetime.now(utc)+timedelta(hours=offset_hours)).strftime(f"%I:%M:%S %p %Z+{offset_hours:02d} %A %d, %B %Y")


def _getTimeOf(arg:str):
	return datetime.now().strftime(arg)

def hourNow():
	return _getTimeOf("%H")

def minuteNow():
	return _getTimeOf("%M")

def secondNow():
	return _getTimeOf("%S")

def getMonthName():
	return _getTimeOf("%B")

def getWeekDayName():
	return _getTimeOf("%A")

def meridiemNow():
	return _getTimeOf("%p")


class Time:
	def __init__(self):
		pass

if __name__ == '__main__':
	#print(_getTimeOf("%H:%M:%S"))
	print(now())
	print(getutc(6))
