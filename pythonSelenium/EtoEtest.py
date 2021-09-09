from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# To login
driver.implicitly_wait(10)
driver.get("https://platform.wyscout.com/app/?")
driver.find_element_by_xpath("//input[@type='text']").send_keys("ravinishad007@gmail.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("")   # use suitable password
driver.find_element_by_xpath("//button[@id='login_button']").click()
driver.find_element_by_xpath("//div[@id='detail_0_home_tab_others']").click()
countries = driver.find_element_by_xpath("//div[@command='area_detail']")
# iterate over countries
for country in countries:
    countryName = country.find_element_by_xpath("//div[@command='area_detail']/div").click()
    if countryName == "Angola":
        country.find_element_by_xpath("//div[@commandsource='list@team_list.nationals@0']").click()

