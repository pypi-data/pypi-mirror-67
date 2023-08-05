import os
import sys

def real_path(filename):
	return os.path.dirname(os.path.abspath(sys.argv[0])) + f"/{filename}"
