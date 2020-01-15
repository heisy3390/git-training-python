# startmodule.py:
import datetime

timeStrFormat = "{0:%Y-%m-%d %H:%M:%S}"
startTime = datetime.datetime.now()

def start():
	print("start : " + timeStrFormat.format(startTime))

def end():
	endTime = datetime.datetime.now()
	print("end : " + timeStrFormat.format(endTime))
	print("span : " + str(endTime - startTime))
