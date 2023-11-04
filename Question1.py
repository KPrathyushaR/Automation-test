import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://subscription.packtpub.com/register")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(6)
print(driver.title)
# login the credentials
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='login-input-email']").send_keys("koppalaprathyusha11197@gmail.com")
driver.find_element(By.XPATH, "//*[@id='login-input-password']").send_keys("Prathyu@123")
sign_in = driver.find_element(By.XPATH, "//*[@id='login-form']/form/button[1]/span")
driver.execute_script("arguments[0].click();", sign_in)
time.sleep(10)

# checking the Navigation elements
driver.find_element(By.XPATH,"//*[@id='packt-navbar']").click()
time.sleep(2)
# Browsering the library
driver.find_element(By.XPATH, "//*[@id='packt-navbar']/div[1]/a").click()
driver.back()
# Advanced Searching
driver.find_element(By.XPATH, "//button[normalize-space()='Advanced Search']").click()
driver.back()
time.sleep(5)
# Selecting the My library dropdown menu
driver.find_element(By.XPATH, "//*[@id='library-dropdown']").click()
time.sleep(5)
# Recent dropdown
driver.find_element(By.XPATH, "//a[@id='recent-dropdown']").click()
time.sleep(5)
# Checking the account page
driver.find_element(By.XPATH, "//a[@class='user-account nav-link']//div").click()
time.sleep(15)
driver.back()
# Checking the checkout page is redirecting to the another page
driver.find_element(By.XPATH, "//div[@class='btn-content']//*[name()='svg']").click()
time.sleep(15)
driver.back()

links = driver.find_elements(By.TAG_NAME, "a")
print("Total Number of links:", len(links))

for link in links:
    print(link.text)

#Scrolling the window
scroll_value= driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(10)

# Sign Out the browser
sign_out = driver.find_element(By.XPATH, "//*[@id='packt-navbar']/div[4]/a[3]")
driver.execute_script("arguments[0].click();", sign_out)
time.sleep(10)





























sign_out = driver.find_element(By.XPATH,"//*[@id='packt-navbar-nav']/div/a[3]")
driver.execute_script("arguments[0].click();", sign_out)
driver.close()



