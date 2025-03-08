import sys
from collections import deque

def print_tail(file, deque_size):
    q = deque(file, maxlen=deque_size)
    for line in q:
        print(line, end='')

args = sys.argv
file = None
if len(args) >= 2:
    need_name = len(args) > 2
    for filename in args[1:]:
        try:
            file = open(filename, 'r')
        except FileNotFoundError as error:
            print(f"tail.py: {error}")
            exit(1)
        if need_name:
            print("==>",filename,"<==")
        print_tail(file, 10)
        file.close()
else:
    file = sys.stdin
    print_tail(file, 17)



