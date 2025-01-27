from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=driver_options)
driver.maximize_window()
scrap_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url=scrap_url)

# number = driver.find_element(By.CSS_SELECTOR, value="#mp-welcomecount ul a")
# number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# number.click()
# print(number.text)

# telephone = driver.find_element(By.CSS_SELECTOR, value="div .mp-contains-float p b")
# telephone.click()
# print(telephone.text)

# ======================= find element by link text =======================
# lady_gaga = driver.find_element(By.LINK_TEXT, value="Lady Gaga")
# lady_gaga.click()
# print(lady_gaga.text)

# ======================= Type in search bar =======================
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)
































# driver.quit()
