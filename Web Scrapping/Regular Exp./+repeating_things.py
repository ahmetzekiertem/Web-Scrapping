import re



# +  character -- this specifies that the previous character can be matched one or more times

# difference from * -- 0 - infinity         + 1 - infinity

regex = re.compile('a+')

#print(regex.match('aaaaaaaaa'))


# using character classes


regex = re.compile('[a-c]*')

print(regex.match(''))
