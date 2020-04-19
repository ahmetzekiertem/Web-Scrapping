import re



# re.compile(pattern)       -- returns a regex object

regex = re.compile('[+]')



# regex.match(string to match) -- returns None if no match else returns a match object





# character class




# complement the set [^pattern]

print(regex.match('+'))


# all metacharacters lose their meaning inside a character class
