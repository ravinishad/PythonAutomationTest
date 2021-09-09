from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# To login
driver.implicitly_wait(10)
driver.get("https://platform.wyscout.com/app/?")
driver.find_element_by_xpath("//input[@type='text']").send_keys("ravinishad007@gmail.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("")  # use suitable password
driver.find_element_by_xpath("//button[@id='login_button']").click()

# Scrolls down
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
 