# Process file: EAFP - >> more PYTHONIC


import os

p = "/path/to/datafile.dat"

try:
    process_file(p)
except OSError as error:
    print(f"Error: {error}")
