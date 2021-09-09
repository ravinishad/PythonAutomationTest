
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# To login
driver.implicitly_wait(10)
driver.get("https://platform.wyscout.com/app/?")
driver.find_element_by_xpath("//input[@type='text']").send_keys("ravinishad007@gmail.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("")  # use suitable password
driver.find_element_by_xpath("//button[@id='login_button']").click()
driver.implicitly_wait(10)
# Checks logout functionality
driver.find_element_by_xpath("//div[@class='account_thumb']").click()
driver.find_element_by_xpath("//a[@command='logout']").click()
