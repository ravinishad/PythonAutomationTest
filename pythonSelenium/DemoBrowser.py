from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe") # For Firefox Browser.
driver.maximize_window() #maximize the window
driver.get("https://platformrc.wyscout.com/app/") # hits url on browser

print(driver.title)     # prints the title of web page.
print(driver.current_url)   # verify weather I have landed in the correct url
driver.refresh()    # to Refresh the page
driver.minimize_window()  # will minimize the window. Note- Run this in debug mode.
driver.close()      # will close the browser. Note: Comment this line when needed
