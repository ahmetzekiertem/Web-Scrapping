import re



# ? question mark -- says the previous character can either come once or not at all

regex = re.compile('a?b')           # min - 0       max - 1

# print(regex.match('aab'))


# {m,n}    m and n are integer values   -- This qualifier means there must be at least m repetitions, and at most n

regex = re.compile('a{2,4}')            # aa aaa aaaa

#print(regex.match('aaaaa'))



# * {0,}

regex = re.compile('a{0,}')

#print(regex.match('aaaaaaaa'))

# + {1,}




# ? {0,1}
