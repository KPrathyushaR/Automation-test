import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://subscription.packtpub.com/")
driver.maximize_window()
time.sleep(6)

driver.execute_script("window.scrollBy(0,650)", " ")
value = driver.execute_script("return window.pageYOffset")
print("Number of pixels moved:", value)
time.sleep(10)

# writing the carousel below the main tile are correctly appearing
driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div[3]/div[3]/div/div/div/div[1]/div/div").click()