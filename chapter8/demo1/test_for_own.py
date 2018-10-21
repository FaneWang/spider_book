from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.get("https://account.geetest.com/register")
wait = WebDriverWait(browser,20)
email = wait.until(EC.presence_of_element_located((By.ID,'email')))
email.send_keys("dsafs@qq.cs")

button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
button.click()

img = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
time.sleep(2)
location = img.location
size = img.size
print(location)
print(location['y'])
print(location['x'])
print(size['height'])
print(size['width'])
top,bottom,left,right = location['y'],location['y'] + size['height'],location['x'],location['x'] + size['width']
print(top,bottom,left,right)

# browser.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Chrome()
# browser.get("https://www.taobao.com")
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, "q")))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-search")))
# print(input, button)
# browser.close()