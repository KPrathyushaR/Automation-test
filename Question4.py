import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.get("https://subscription.packtpub.com/register")
driver.maximize_window()
time.sleep(6)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='login-input-email']").send_keys("koppalaprathyusha11197@gmail.com")
driver.find_element(By.XPATH, "//*[@id='login-input-password']").send_keys("Prathyu@123")
sign_in = driver.find_element(By.XPATH, "//*[@id='login-form']/form/button[1]/span")
driver.execute_script("arguments[0].click();", sign_in)
time.sleep(10)

driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[3]/div[1]/div/div[2]/a").click()
time.sleep(10)

Search_bar = driver.find_element(By.XPATH, "//input[@placeholder='Search titles …']")
Search_bar.send_keys("Machine Learning Engineering with Python - Second Edition")
act = ActionChains(driver)
act.double_click(Search_bar).perform()
driver.back()
time.sleep(5)

alllinks = driver.find_elements(By.TAG_NAME,'a')
count = 0
for link in alllinks:
    Url = link.get_attribute('href')
    try:
        res= request.head(url)
    except:
        none
    if res.status_code>=400:
        print(url,"is broken link")
        count+=1
    else:
        print(url, "is valid link")

