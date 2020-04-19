import re



# ^ character   -- says that the string should start with
regex = re.compile('^abc')


# | character -- is the or operator

regex = re.compile('a|b')

# $ character -- matches the end of line

regex = re.compile('abc$')
