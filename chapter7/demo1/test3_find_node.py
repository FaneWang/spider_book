from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
# input_first = browser.find_element_by_id("q")
# input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# input_fourth = browser.find_element(By.ID,"q")
# print(input_first,input_second,input_third,input_fourth)

lis = browser.find_elements_by_css_selector(".sevice-bd li")
lis2 = browser.find_elements(By.CSS_SELECTOR,".service-bd li")
print(lis)
browser.close()