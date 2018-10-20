from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get("http://www.onepig.top/")
except TimeoutExcetion as e:
    print("Time out : " + str(e))
try:
    browser.find_element_by_id("hello")
except NoSuchElementException as e:
    print("No element : " + str(e))
finally:
    browser.close()