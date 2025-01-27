from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome driver open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
url = "https://www.python.org/"
driver.get(url=url)

# ====================================================================

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"{price_dollar.text}.{price_cents.text}")
# ====================================================================

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar)
print(search_bar.tag_name)     # input
print(search_bar.get_attribute("placeholder"))       # Search
print(search_bar.get_attribute("role"))       # textbox
print("==================================")

button = driver.find_element(By.ID, value="submit")
print(button.size)
print(button.text)
print("==================================")

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)
print("==================================")

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)
print(bug_link.get_attribute("href"))

# ====================================================================

# driver.close() # closes single tab
driver.quit()  # closes all tabs




















