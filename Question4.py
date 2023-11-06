import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.get("https://subscription.packtpub.com/")
driver.implicity_wait(5)
driver.maximize_window()
time.sleep(6)
#browsing the top navigation page
driver.find_element(By.XPATH, "//*[@id='packt-navbar-nav']/div/a[1]").click()
time.sleep(10)
#resetting the browser page
driver.find_element(By.XPATH, "//*[@id='root']/div/div[5]/div[1]/div[1]/button").click()
driver.refresh()
#clicking the publisher year
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div[1]/div[4]/div/img").click()
#Filtering the 2021 books
driver.find_element(By.XPATH, "//*[@id='root']/div/div[5]/div[1]/div[4]/div[2]/div[4]/div[1]").click()

#Searching the titles
Search_bar = driver.find_element(By.XPATH, "//*[@id='search-input']/input").clear()
Search_bar.send_keys("Python")
act = ActionChains(driver)
act.double_click(Search_bar).perform()
driver.back()
time.sleep(5)
print(search_bar)

driver.refresh()
search_bar.send_keys("Paint")
act = ActionChains(driver)
act.double_click(Search_bar).perform()
driver.back()
time.sleep(5)
print(search_bar)

driver.refresh()
search_bar.send_keys("secure")
act = ActionChains(driver)
act.double_click(Search_bar).perform()
driver.back()
time.sleep(5)
print(search_bar)

driver.refresh()
search_bar.send_keys("tableau")
act = ActionChains(driver)
act.double_click(Search_bar).perform()
driver.back()
time.sleep(5)
print(search_bar)

driver.close()





