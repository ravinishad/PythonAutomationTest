from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# To login
driver.implicitly_wait(10)
driver.get("https://platform.wyscout.com/app/?")
driver.find_element_by_xpath("//input[@type='text']").send_keys("ravinishad007@gmail.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("")     # use suitable password
driver.find_element_by_xpath("//button[@id='login_button']").click()
driver.maximize_window()
# testing menu Functionality
driver.find_element_by_xpath("//div[@id='b_app_switcher']").click()
driver.find_element_by_xpath("//div[@title='Platform']").click()
