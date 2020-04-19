from bs4 import BeautifulSoup



def read_file():
    file = open('intro_to_soup_html.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# Navigable strings


# string inside a tag   - .string

title = soup.title

#print(title)

#print(title.string)



# .replace_with("") function            -- navigable string

print(title)

title.string.replace_with("title has been changed")


print(title)
