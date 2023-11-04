from selenium.webdriver.support.color import Color

rgb = find_element_by_class_name("bar").value_of_css_property('background-color')
hex = Color.from_string(rgb).hex



boolean eleSelected= driver.findElement(By.xpath("xpath")).isDisplayed();