from bs4 import BeautifulSoup
import re


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# most popular methods

# find()
# find_all()        -- to keep it simple for now, it takes the tag name as parameter



# Kinds of filters which we can use to retrieve tags - filters sent as parameter to find/find_all methods

# string

#print(soup.find_all('a'))

# regular expression

# tag names start with b

regex = re.compile('^b')

for tag in soup.find_all(regex):
    #print(tag.name)
    pass


# tag names contains t

regex = re.compile('t')

for tag in soup.find_all(regex):
    #print(tag.name)
    pass


# list

# all a and b tags

for tag in soup.find_all(['a','b']):
    #print(tag.name)
    pass


# function

# just giving an example here - we'll discuss this more when we implement find_all

def has_class(tag):
    return tag.has_attr('class')

for tag in soup.find_all(has_class):
    print(tag.name)
