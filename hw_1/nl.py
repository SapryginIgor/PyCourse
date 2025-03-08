import sys

args = sys.argv
file = None
if len(args) > 2:
    raise NotImplementedError("many files aren't supported")
elif len(args) == 2:
    filename = args[1]
    try:
        file = open(filename, 'r')
    except FileNotFoundError as error:
        print(f"nl.py: {error}")
        exit(1)
else:
    file = sys.stdin
cnt = 1
for line in file:
    print(f"     {cnt}  " + line, sep='')
    cnt+=1
file.close()



