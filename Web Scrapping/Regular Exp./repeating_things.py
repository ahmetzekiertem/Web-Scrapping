import re



# * character - this specifies that the previous character can be matched zero or more times, instead of exactly once.

regex = re.compile('[a-c]*')       # -- lower limit is 0 and the upper limit is infinity


print(regex.match('caaaaaaaaaaabcaaaaa'))
