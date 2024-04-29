from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

scripDir=os.path.dirname(__file__)
os.chdir(scripDir)

options = webdriver.ChromeOptions()
options.headless=True
driver = webdriver.Chrome(options=options)
driver.get("https://python.org")

searchInput=driver.find_element(by=By.XPATH, value='//*[@id="id-search-field"]')
searchInput.send_keys("django")

searchbutton=driver.find_element(by=By.ID, value="submit")
searchbutton.click()

driver.save_screenshot("python.org.1.png")
driver.find_element(by=By.TAG_NAME, value="body").screenshot("python.org.2.png")

func = lambda arg: driver.execute_script("return document.body.parentNode.scroll"+arg)
driver.set_window_size(func("Width"), func("Height"))
driver.find_element(by=By.TAG_NAME, value="body").screenshot("python.org.3.png")

time.sleep(5)
driver.quit()