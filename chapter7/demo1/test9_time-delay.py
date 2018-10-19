# from selenium import webdriver

# browser = webdriver.Chrome()

# browser.implicitly_wait(10)
# browser.get("https://www.zhihu.com/explore")
# input = browser.find_element_by_class_name("zh-top-add-question")
# print(input)
# browser.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, "q")))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-search")))
print(input, button)
browser.close()