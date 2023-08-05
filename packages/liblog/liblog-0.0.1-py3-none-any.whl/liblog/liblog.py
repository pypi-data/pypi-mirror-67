import sys
import threading

lock = threading.RLock()

CN = "\033[K"
CC = "\033[0m"

def log(value):
	with lock:
		print(f"{CN}{value}{CC}")

def log_replace(value):
	sys.stdout.write(f"{CN}{value}{CC}\r")
	sys.stdout.flush()