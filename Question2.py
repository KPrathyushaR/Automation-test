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
time.sleep(10)
driver.back()

playlist = driver.find_element(By.XPATH, "//*[@id='packt-navbar-nav']/div/div[1]/div/a[2]/span")
playlist.click()
time.sleep()
driver.back()

# Checking the advanced Browser
driver.find_element(By.XPATH, "//*[@id='packt-navbar-nav']/div/a[2]").click()

driver.find_element(By.XPATH, "//*[@id='title']").send_keys("Python")

#Checkboxes 
checkboxes = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div[3]/div[3]/div/div/header/button")
checkboxes.click() 
print(len(checkboxes))

for i in range():
  print("Selected the Checkboxes", checkboxes)
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






