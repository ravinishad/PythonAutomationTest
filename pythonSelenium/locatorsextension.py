from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://platformrc.wyscout.com/app/")

driver.find_element_by_css_selector("#username").send_keys("ravinishad007@gmail.com")

driver.find_element_by_css_selector(".new-login-input").send_keys("ravi")

driver.find_element_by_css_selector(".new-login-input").clear()
driver.find_element_by_link_text("Lost your password?").click()    # identifying link

