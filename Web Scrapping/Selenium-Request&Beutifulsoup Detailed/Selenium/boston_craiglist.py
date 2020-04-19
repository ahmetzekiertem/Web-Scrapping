import requests

from fake_useragent import UserAgent

from bs4 import BeautifulSoup

#Create user agent

ua = UserAgent()



#Create a header with the useragent

#header = {'user-agent':ua.chrome}



#requests.get(url)  --- response object with useragent and timeout

response = requests.get('https://boston.craigslist.org/search/sof', headers=header)



#parse html page with beautiful

soup = BeautifulSoup(response.content,'lxml')



attr ={'class':'result-title hdrlnk'}



tag_a = soup.find_all('a',attrs=attr)

for i in tag_a:
    print("Job: " + i.string + "\n" + "URL: " + str(i['href']))

    print('\n')
