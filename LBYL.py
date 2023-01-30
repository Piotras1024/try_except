# Process file: LBYL - >> less PYTHONIC


import os

p = "/path/to/datafile.dat"

if os.path.exists(p):
    process_file(p)
else:
    print(f"no such directory as p = {p}")
