import re
line = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").
a=". "
b=".\n"
result = re.split(r'[;,\s]', line)
print (result,a,b)

