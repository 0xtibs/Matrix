import random
import os
import time
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

delay_print("Neo.......መ ቀ ስ ቀ ስ    ት ፈ ል ጋ ለ ህ ን???")
print("\n")

ans = input("Y/N?")

if ans == "Y":


	rows, columns = os.popen('stty size', 'r').read().split()

	chars_to_print = ['ፊ', 'ደ', 'ል','፩','፪','፫','፬','፭','፷','፶','፶','፵','፴','ዘ','ዱ','ሓ']
	colors = ["\033[01;32m", "\033[00;32m", "\033[00;32m", "\033[00;30m"]


	line_width = int(columns)

	while True:
		for i in range(line_width):
			print(random.choice(colors),random.choice(chars_to_print),sep='  ',end='')
		print()
	time.sleep(0.05)
