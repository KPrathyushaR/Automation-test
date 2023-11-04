import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://subscription.packtpub.com/advanced-search")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH, "//div[@class='orange advanced-search__search-form__clear-all ml-auto']").click()

#Title of the content
add = driver.find_element(By.ID, "title").send_keys("python")
act = ActionChains(driver)
act.context_click(add).perform()
print(add)

author = driver.find_element(By.XPATH, "//*[@id='content-author']").send_keys("Aleksander Molak")
act = ActionChains(driver)
act.context_click(author).perform()
print(author)






