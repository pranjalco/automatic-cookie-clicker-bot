from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from art import logo

"""
# Project 33:Automatic Cookie Clicker Bot

## Author
- **Name**: Pranjal Sarnaik  
- **Date**: 27 Jan 2025  

## Description
An automated game-playing bot created using Selenium and Python to play the **Cookie Clicker** game. The bot clicks the cookie continuously, evaluates affordable upgrades every 5 seconds, and buys the most expensive one to maximize cookies per second. The bot stops after 5 minutes and displays the "cookies/second" rate achieved during the session.

## How to Use
1. Visit the game website: [Cookie Clicker Classic Version](http://orteil.dashnet.org/experiments/cookie/).  
2. Run the bot to automate gameplay, and let it manage upgrades for the best performance.  
3. Observe how efficiently the bot increases cookies per second!  

## Level
- **Level**: Intermediate  
- **Skills**: Python, Selenium, Automation  
- **Domain**: Game Bot Development  

## Features
- Automates cookie clicking.  
- Checks for affordable upgrades every 5 seconds.  
- Prioritizes the most expensive upgrade within budget.  
- Stops after 5 minutes and displays the cookies-per-second rate achieved.  

## Installation
1. Clone this repository:  
   ```bash
   git clone https://github.com/pranjalco/automatic-cookie-clicker-bot.git
   ```  

2. Navigate to the project directory:  
   ```bash
   cd automatic-cookie-clicker-bot
   ```  

3. Install the required libraries:  
   ```bash
   pip install selenium
   ```  

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.  
2. Open the terminal and navigate to the project folder.  
3. Execute the program:  
   ```bash
   app.py
   ```  

## File Structure
- **app.py**: The main bot script.  
- **experiments/**: Temporary or practice files.  
- **screenshots/**: Program screenshots.  
- **README.md**: Project documentation.  

## Output
- After 5 minutes, the bot stops and displays the "cookies/second" rate in the terminal.  

---

**Created by Pranjal Sarnaik**  
*© 2025. All rights reserved.*  
"""

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=driver_options)
driver.maximize_window()
scrap_url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url=scrap_url)

# Here by using this element we can click on cookie
cookie = driver.find_element(By.ID, value="cookie")

# Collect upgrade item ids
upgrade_items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
# item_ids = [item.get_attribute("id") for item in items]

upgrade_item_ids = []
for items in upgrade_items:
    upgrade_item_ids.append(items.get_attribute("id"))
    # below is the output of above code
# ['buyCursor', 'buyGrandma', 'buyFactory', 'buyMine', 'buyShipment',
# 'buyAlchemy lab', 'buyPortal', 'buyTime machine', 'buyElder Pledge']

# Get current time
start_time = time.time()
calculate_total_time = 0
end_time = 60 * 1  # These are 5 minutes

# ==============================================================================

print(logo)
while True:

    cookie.click()

    if time.time() > (start_time + 5):

        calculate_total_time += 5
        start_time = time.time()
        print("")
        print("=====================================================================")
        print("5 sec elapsed")

        # Find all upgrade prices
        all_upgrade_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        upgrade_prices = []

        # Calculate int prices of each upgrade.
        for prices in all_upgrade_prices:
            if prices.text != "":
                int_prices = int(prices.text.split("-")[1].strip().replace(",", ""))
                upgrade_prices.append(int_prices)
                # This upgrade_prices will have output like this:
                # [15, 100, 500, 2000, 7000, 50000, 1000000, 123456789]

        # Creating dictionary containing cost and name of id
        upgrades_info = {}
        for i in range(len(upgrade_prices)):
            upgrades_info[upgrade_prices[i]] = upgrade_item_ids[i]

        # Get how many cookies you have currently
        total_cookies = driver.find_element(by=By.ID, value="money").text
        if "," in total_cookies:
            total_cookies = total_cookies.replace(",", "")
        my_total_cookies = int(total_cookies)
        print(my_total_cookies)

        # Finding which updates we can do based on our current cookie count.
        upgrades_we_can_do = {}
        for money, id in upgrades_info.items():
            if my_total_cookies > money:
                upgrades_we_can_do[money] = id
        print("Updates we can do based on our current cookie count.")
        print(upgrades_we_can_do)

        # Purchasing the most expensive upgrade which we can buy from "upgrades_we_can_do" dictionary.
        if upgrades_we_can_do:
            expensive_upgrade = max(upgrades_we_can_do)
            print("The most expensive upgrade which we can buy from 'upgrades_we_can_do' dictionary")
            print(expensive_upgrade)
            purchase_id = upgrades_we_can_do[expensive_upgrade]
            print("Id of upgrade which we are going to buy")
            print(purchase_id)

            # Clicking on upgrade to buy it
            print(f"Clicking on upgrade {purchase_id} to buy it")
            driver.find_element(By.ID, value=purchase_id).click()
        else:
            print("List is empty")

        print("Checking if 5 minutes are completed or not.")
        print(f"Total time elapsed: {calculate_total_time} Sec")
        print(f"We have to stop at {end_time} seconds, means 5 minutes.")

    if calculate_total_time > end_time:
        print("")
        print("=================== Completed =======================")
        print("5 minutes completed!")
        print("Quiting the program")
        cookie_per_second = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_second)
        break

# ==============================================================================
