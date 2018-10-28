from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'domain','value':'fane'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())