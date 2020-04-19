from bs4 import BeautifulSoup



def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

body = soup.body
p = soup.body.p


# body - contents


#print(body.contents)


# .next_sibling


print(p.next_sibling.next_sibling)
