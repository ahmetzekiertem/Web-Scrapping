from bs4 import BeautifulSoup
import re


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# Signature: find_all(name, attrs, recursive, string, limit, **kwargs)

# string parameter


regex = re.compile('story')

tag = soup.find_all(string=regex)



# **kwargs arguments

tags = soup.find_all(class_='story')


# to write the class attribute of a tag - use       class_          because simple class is a keyword in Python


# recursive parameter


title = soup.find_all('title',recursive=False)

print(title)
