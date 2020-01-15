# main.py:
from debugmodule import *
import teama.member1

def callFirst():
	start()

def callLast():
	end()

if __name__ == '__main__':
	callFirst()
	teama.member1.process1()
	teama.member1.process2()
	callLast()
