






from selenium import webdriver      # imports
from time import sleep
from bs4 import BeautifulSoup


# make a webdriver object   -    chrome driver path for my system -- >    /Users/waqarjoyia/Downloads/chromedriver


driver = webdriver.Chrome('/Users/mac/Desktop/geckodriver')

# open some page using get method       - url -- > parameters





# close webdriver object

driver.close()
