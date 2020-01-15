# main.py:
from debugmodule import *

import teama.member1
import teama.member2

import teamb.member1
import teamb.member2

import teamc.member1
import teamc.member2

import teamd.member1
import teamd.member2

import teame.member1
import teame.member2


def callFirst():
	start()

def callLast():
	end()

if __name__ == '__main__':
	callFirst()

	teama.member1.process1()
	teama.member1.process2()
	teama.member2.process1()
	teama.member2.process2()

	teamb.member1.process1()
	teamb.member1.process2()
	teamb.member2.process1()
	teamb.member2.process2()

	teamc.member1.process1()
	teamc.member1.process2()
	teamc.member2.process1()
	teamc.member2.process2()

	teamd.member1.process1()
	teamd.member1.process2()
	teamd.member2.process1()
	teamd.member2.process2()

	teame.member1.process1()
	teame.member1.process2()
	teame.member2.process1()
	teame.member2.process2()

	callLast()
