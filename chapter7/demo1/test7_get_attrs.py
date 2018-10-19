from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = "https://www.zhihu.com/explore"
browser.get(url)
# logo = browser.find_element_by_id("zu-top-link-logo")
# print(logo)
# print(logo.get_attribute("class"))
input = browser.find_element_by_class_name("zu-top-add-question")
print(input.text)
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)

browser.close()