from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=driver_options)
driver.maximize_window()
scrap_url = "https://secure-retreat-92358.herokuapp.com/"
driver.get(url=scrap_url)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Pranjal")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("IsProgram")

email = driver.find_element(By.NAME, value="email")
email.send_keys("pranjal@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value=".form-signin button")
submit.click()









driver.quit()


























