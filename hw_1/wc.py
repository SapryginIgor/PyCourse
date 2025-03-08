import sys
from collections import deque

def make_wc(file):
    s = file.read()
    num_bytes = len(s)
    s = str(s)
    lines = s.splitlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words, num_bytes

args = sys.argv
file = None
if len(args) >= 2:
    need_total = len(args) > 2
    total_bytes = 0
    total_words = 0
    total_lines = 0
    for filename in args[1:]:
        try:
            file = open(filename, 'r')
        except FileNotFoundError as error:
            print(f"wc.py: {error}")
            exit(1)
        num_bytes, num_words, num_lines = make_wc(file)
        print(" {}\t{}\t{} ".format(num_lines, num_words, num_bytes) + filename)
        if need_total:
            total_bytes += num_bytes
            total_lines += num_lines
            total_words += num_words

        file.close()
    if need_total:
        print(" {}\t{}\t{} ".format(total_lines, total_words, total_bytes) + 'total')
else:
    file = sys.stdin
    print(" {}\t{}\t{}".format(*make_wc(file)))



