import requests

from bs4 import  BeautifulSoup


url = "https://yellowpages.com.tr/ara?q=Ankara"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

#print(soup.prettify()) # Print Functions for show all documents of url

for i in soup.find_all("a"):
    print(i.text)
    print("****************")



print(soup.find_all("div",{"class":"yp-poi-box-2"}))







