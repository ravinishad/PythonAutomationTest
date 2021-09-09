from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# To login
driver.implicitly_wait(10)
driver.get("https://platform.wyscout.com/app/?")
driver.find_element_by_xpath("//input[@type='text']").send_keys("ravinishad007@gmail.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("")  # use suitable password
driver.find_element_by_xpath("//button[@id='login_button']").click()

# selects country
#driver.implicitly_wait(5)
driver.find_element_by_xpath("//div[@commandsource='list@area_list@5']").click()
driver.find_element_by_xpath("//div[@commandsource='list@competition_list@0']").click()
driver.find_element_by_xpath("//div[@commandsource='list@team_list@0']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//div[@id='detail_0_team_back']").click()     # Checks back button functionality