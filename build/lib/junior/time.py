from datetime import datetime,timedelta
from pytz import utc



def today():
	return str(date.today())

def currentTime():
	return datetime.now()

def now():
	return datetime.now(utc).strftime("%H:%M:%S %p %Z %A %d %B %Y")

def getUtcTextFormat(offset_hours):
	return (datetime.now(utc)+timedelta(hours=offset_hours)).strftime(f"_%H_%M_%S_%Y_%m_%d") 

def getutc(offset_hours):
    # Get the current UTC time
	return (datetime.now(utc)+timedelta(hours=offset_hours)).strftime(f"%I:%M:%S %p %Z+{offset_hours:02d} %A %d %B %Y")

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


if __name__ == '__main__':
	pass