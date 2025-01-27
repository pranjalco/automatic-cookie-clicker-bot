from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
scrap_url = "https://www.python.org/"
driver.get(scrap_url)

date_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu time")
event_name_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu a")
events = {}

for n in range(len(date_list)):
    events[n] = {
        "date": date_list[n].text,
        "name": event_name_list[n].text
    }

print(events)
driver.quit()

# This is the answer
output = {0: {'date': '2025-01-27', 'name': 'Python Leiden User Group'},
          1: {'date': '2025-01-29', 'name': 'IndyPy - Building Voice Agents: Unpacking the Pipeline'},
          2: {'date': '2025-02-02', 'name': 'Python devroom @ FOSDEM 2025'},
          3: {'date': '2025-02-08', 'name': 'PyCascades 2025'},
          4: {'date': '2025-02-15', 'name': 'Python Barcamp Karlsruhe 2025'}}
