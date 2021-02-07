from selenium import webdriver

driver_location = "/home/anima/Рабочий стол/Python3/Selenium/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)
driver.get("https://www.youtube.com/")
#driver.get("http://127.0.0.1:8000/admin")


print(driver.page_source.encode('utf-8'))
driver.quit()
