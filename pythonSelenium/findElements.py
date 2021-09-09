import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://platformrc.wyscout.com/app/")
driver.find_element_by_xpath("//input[@type='text']").send_keys("ravinishad007@gmail.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("")  # use suitable password
driver.find_element_by_xpath("//button[@id='login_button']").click()
# to search Player or Team
driver.find_element_by_id("global_search_input").send_keys("India")
time.sleep(2)

teams = driver.find_element_by_css_selector("div[class='item-element item-text title'] a")
print(len(teams))
# searches for team
for team in teams:
    if team.text == "India":
        team.click()
        break
# verifies if match happens
assert driver.find_element_by_id("global_search_input").get_property('value') == "India"
