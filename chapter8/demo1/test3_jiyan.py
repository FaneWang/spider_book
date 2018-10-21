from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains
from PIL import Image
from io import BytesIO

EMAIL = "test@test.com" 
BORDER = 6

class CrackGeetest():
    def __init__(self):
        self.url = "https://account.geetest.com/register"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,20)
        self.email = EMAIL
    def __del__(self):
        self.browser.close()

    def getGeetestButton(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button

    def getPosition(self):
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top,bottom,left,right = location['y'],location['y'] + size['height'],location['x'],location['x'] + size['width']
        return(top,bottom,left,right)
    
    def getScreenshot(self):
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def getGeetestImage(self,name='captcha.png'):
        top,bottom,left,right = self.getPosition()
        print('验证码位置',top,bottom,left,right)
        screenshot = self.getScreenshot()
        captcha = screenshot.crop((left,top,right,bottom))
        captcha.save(name)
        return captcha
    
    def getSlider(self):
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_slider_button')))
        return slider

    def isPixelEqual(self,image1,image2,x,y):
        pixel1 = image1.load()[x,y]
        pixel2 = image2.load()[x,y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def getGap(self,image1,image2):
        left = 60
        for i in range(left,image1.size[0]):    
            for j in range(image1.size[1]):
                if not self.isPixelEqual(image1,image2,i,j):
                    left = i
                    # return left
        return left

    def getTrack(self,distance):
        track = []
        current = 0
        mid = distance * 4 /5
        t = 0.2 
        v = 0
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            v = v0 + a*t
            move = v0*t + 1/2*a*t*t
            current += move
            track.append(round(move))
        return track

    def moveToGap(self,slider,tracks):
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x,yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()
    def open(self):
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID,'email')))
        email.send_keys(self.email)

    def register(self):
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'login-btn')))
        submit.click()
        time.sleep(10)
        print("注册成功")
    def crack(self):
        self.open()
        button = self.getGeetestButton()
        button.click()
        image1 = self.getGeetestImage('captcha1.png')
        slider = self.getSlider()
        slider.click()
        image2 = self.getGeetestImage('captcha2.png')
        gap = self.getGap(image1,image2)
        print('缺口位置',gap)
        gap -= BORDER
        track = self.getTrack(gap)
        print("滑块轨迹",track)
        self.moveToGap(slider,track)

        success = self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,'geetest_success_radar_tip_content'),'验证成功'))
        print(success)
        if not success:
            self.crack()
        else:
            self.register()

if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()