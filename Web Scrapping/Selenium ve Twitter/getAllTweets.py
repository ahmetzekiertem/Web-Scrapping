from selenium import webdriver
import loginInfo
import time


browser = webdriver.Firefox()

browser.get("https://twitter.com/")

time.sleep(3)

giris_yap = browser.find_elements_by_css_selector("aqw.r-1fneopy.r-o7ynqc.r-6css-4rbku5.css-18t94o4.css-1dbjc4n.r-1niwhzg.r-p1n3y5.r-sdzlij.r-1phboty.r-rs99b7.r-1loqt21.r-1w2pmg.r-ku1wi2.r-1vuscfd.r-1dhv416eg.r-lrvibr")


giris_yap.click()

time.sleep(5)
