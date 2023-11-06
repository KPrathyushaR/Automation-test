import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://subscription.packtpub.com/")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(5)

#Selecting the Library and options below 
driver.find_element(By.XPATH, "//*[@id='library-dropdown']").click()
time.sleep(10)

home = driver.find_element(By.XPATH, "//*[@id='packt-navbar-nav']/div/div[1]/div/a[1]/span")
home.click()



# searching the title name in the search bar
# driver.find_element(By.XPATH, "//*[@id='search-input']/input").send_keys("python")
# driver.find_element(By.XPATH, "//*[@id='search-input']/img").click()

#scrolling the starting to the end
# driver.execute_script("window.scrollBy(0,456)", " ")
# value = driver.execute_script("return window.pageYOffset")
# print("Number of pixels moved:", value)
# time.sleep(10)
# Checkboxes for the product type
# count = driver.find_element(By.CLASS_NAME, "list-item false")
# print(len(count))






