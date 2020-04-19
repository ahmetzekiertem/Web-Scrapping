import re   # regular expression module



# specialised language which can be used to search for text within a given document with precision and efficiency


# expression -- > compiled into bytecode    --> executed by a matching engine written in C

# Usage :
# Matching Characters


'''

a simple expression matches itself in the given string


Exception --> Metacharacters

They don't match themselves

Complete list of Metacharacters  -->         . ^ $ * + ? { } [ ] \ | ( )


'''

# First Metacharacters which we will look at are --- >        [   ]

'''


# 9


# [12345] - [1-5]





used for specifying a character class   - character class is a set of characters you wish to match

for example if I've written the following regex :

            [xyz]

this will match any x,y or z character

We could also give a range using hyphen,


            [x-z]           --- equivalent to ---              [xyz]



We will discuss more about this in the next video


'''
