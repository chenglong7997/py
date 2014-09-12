import RPi.GPIO as gpio
import time

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(7, gpio.OUT)
	gpio.setup(11, gpio.OUT)
	gpio.setup(13, gpio.OUT)
	gpio.setup(15, gpio.OUT)

def forward(tf):
	init()
	# 7 11 for left side
	gpio.output(7, True)
	gpio.output(11, False)

	#13 15  for right side
	gpio.output(13, True)
	gpio.output(15, False)

	#sleep for tf(timefame)
	time.sleep(tf)
	gpio.cleanup()

def reverse(tf):
	init()
	gpio.output(7, False)
	gpio.output(11, True)
	gpio.output(13, False)
	gpio.output(15, True)

	#sleep for tf(timefame)
	time.sleep(tf)
	gpio.cleanup()

def turn_left(tf):
	init()
	gpio.output(7, True)
	gpio.output(11, True)
	gpio.output(13, True)
	gpio.output(15, False)

	#sleep for tf(timefame)
	time.sleep(tf)
	gpio.cleanup()

def reverse_turn_left(tf):
	init()
	gpio.output(7, True)
	gpio.output(11, True)
	gpio.output(13, False)
	gpio.output(15, True)

	#sleep for tf(timefame)
	time.sleep(tf)
	gpio.cleanup()

def turn_right(tf):
	init()
	gpio.output(7, True)
	gpio.output(11, False)
	gpio.output(13, True)
	gpio.output(15, True)

	#sleep for tf(timefame)
	time.sleep(tf)
	gpio.cleanup()

def reverse_turn_right(tf):
	init()
	gpio.output(7, False)
	gpio.output(11, True)
	gpio.output(13, True)
	gpio.output(15, True)

	#sleep for tf(timefame)
	time.sleep(tf)
	gpio.cleanup()

def pivot_left(tf):
	init()
	gpio.output(7, False)
	gpio.output(11, True)
	gpio.output(13, True)
	gpio.output(15, False)

	#sleep for tf(timefame)
	time.sleep(tf)
	gpio.cleanup()

def pivot_right(tf):
	init()
	gpio.output(7, True)
	gpio.output(11, False)
	gpio.output(13, False)
	gpio.output(15, True)

	#sleep for tf(timefame)
	time.sleep(tf)
	gpio.cleanup()

#pivot_right(1)

turn_left(1)
reverse_turn_left(1)

turn_right(1)
reverse_turn_right(1)


turn_left(1)
reverse_turn_left(1)

turn_right(1)
reverse_turn_right(1)
