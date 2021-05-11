#automation for clicking a photo from camera to post it

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
desired_cap = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appPackage": "com.ATG.World",
    "appWaitActivity": "com.atg.world.activity.IntroActivity",
    "app": "C:\\Users\\Lenovo\\Desktop\\New folder\\app-debug.apk",
    "appWaitDuration": "5000",
    "appExecTimeout": "50000",
    "uiautomator2ServerLaunchTimeout": "50000",
    "uiautomator2ServerInstallTimeout": "50000",
    "driver": "http://localhost:4723/wd/hub",
    "noReset" : True
    }

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(20)
driver.find_element_by_id("com.ATG.World:id/getStartedTv").click()
driver.implicitly_wait(20)
driver.find_element_by_id("com.ATG.World:id/login_email").click()

email = driver.find_element_by_id("com.ATG.World:id/email")
email.send_keys("wiz_saurabh@rediffmail.com")
password = driver.find_element_by_id("com.ATG.World:id/password")
password.send_keys("Pass@123")
signin = driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
signin.click()
print("signin")

time.sleep(10)
#tap first got it
TouchAction(driver).tap(x=171,y=831).perform()
print("skip1")
time.sleep(5)
#tap second got it
TouchAction(driver).tap(x=176,y=1282).perform()
print("skip2")
time.sleep(3)
#tap post icon
TouchAction(driver).tap(x=535,y=1964).perform()
time.sleep(3)
#tap post image
TouchAction(driver).tap(x=723,y=837).perform()
time.sleep(3)
#tap post image from camera
TouchAction(driver).tap(x=527,y=1240).perform()

driver.find_element_by_id("com.android.camera2:id/shutter_button").click()
driver.implicitly_wait(20)
driver.find_element_by_id("com.android.camera2:id/done_button").click()
driver.implicitly_wait(20)
caption = driver.find_element_by_id("com.ATG.World:id/postCaption")
caption.send_keys("Testing Image 1")
post_btn = driver.find_element_by_id("com.ATG.World:id/toolbar_post_action")
post_btn.click()




