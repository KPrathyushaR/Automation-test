

#Title of the content
add = driver.find_element(By.ID, "title").send_keys("python")
act = ActionChains(driver)
act.context_click(add).perform()
print(add)

author = driver.find_element(By.XPATH, "//*[@id='content-author']").send_keys("Aleksander Molak")
act = ActionChains(driver)
act.context_click(author).perform()
print(author)
