from selenium import webdriver
proxy = "125.70.13.77:8080"
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(chrome_options=chromeOptions)
browser.get('http://httpbin.org/get')