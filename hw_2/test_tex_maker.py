from texfunctions.generator import make_tex

table = [['foo', 'bar', 'baz'],
         [10, 10000000, -42],
         ['hello', 'from', 'my package :3']]

file = open('example.tex', 'w')
file.write(make_tex()('header')('picture', 'frog.jpeg', 0.5)('table',table)('footer')('finalize'))
file.close()