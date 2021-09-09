from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://platformrc.wyscout.com/app/")

driver.find_element_by_name("username").send_keys("ravinishad007@gmail.com")  # Enters detail in the edit box
driver.find_element_by_name("password").send_keys("xyz")
driver.find_element_by_xpath("//button[@command='login_submit']").click()
#finding element by css selector
#driver.find_element_by_css_selector("input[name='username']").send_keys("ravinishad007@gmail.com")


