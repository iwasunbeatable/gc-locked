from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Settings
INSTAGRAM_USERNAME = 'hmu.brachorr'
INSTAGRAM_PASSWORD = 'sammy2301@@@@'
GROUP_CHAT_URL = 'https://www.instagram.com/direct/t/1184750303514319/'  # Your group chat URL
LOCKED_GROUP_NAME = 'Your Locked Group Name'

def login(driver):
    driver.get('https://www.instagram.com/accounts/login/')
    wait = WebDriverWait(driver, 15)
    # Wait for username input
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
    password_input = driver.find_element(By.NAME, 'password')
    username_input.send_keys(INSTAGRAM_USERNAME)
    password_input.send_keys(INSTAGRAM_PASSWORD)
    password_input.send_keys(Keys.RETURN)
    # Wait for main page to load after login
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'nav')))
    print("Logged in successfully")

def check_and_lock_group_name(driver):
    driver.get(GROUP_CHAT_URL)
    wait = WebDriverWait(driver, 15)

    # Wait for Chat Details button and click it
    chat_details_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Chat details"]')))
    chat_details_button.click()
    print("Opened chat details")
    time.sleep(2)  # wait for the panel to open

    # Wait for input box of group name (adjust selector if needed)
    group_name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Name this group chat"]')))
    current_name = group_name_input.get_attribute('value')

    if current_name != LOCKED_GROUP_NAME:
        group_name_input.clear()
        group_name_input.send_keys(LOCKED_GROUP_NAME)
        group_name_input.send_keys(Keys.RETURN)
        print(f'Group name changed back to locked name: {LOCKED_GROUP_NAME}')
    else:
        print('Group name is already locked.')

    time.sleep(2)

def main():
    driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
    try:
        login(driver)
        while True:
            check_and_lock_group_name(driver)
            # Wait 60 seconds before checking again
            time.sleep(60)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
