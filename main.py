from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Settings
INSTAGRAM_USERNAME = 'hmu.brachorr'
INSTAGRAM_PASSWORD = 'sammy2301@@@@'
GROUP_CHAT_URL = 'https://www.instagram.com/direct/t/1184750303514319/'  # Replace with your group chat URL
LOCKED_GROUP_NAME = 'Your Locked Group Name'

def login(driver):
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    username_input.send_keys(INSTAGRAM_USERNAME)
    password_input.send_keys(INSTAGRAM_PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait to log in

def check_and_lock_group_name(driver):
    driver.get(GROUP_CHAT_URL)
    time.sleep(5)

    # Open group chat info - modify selector as per actual Instagram UI
    info_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Chat Details"]')
    info_button.click()
    time.sleep(3)

    # Find the group chat name input field and get current name - adjust selector
    group_name_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Group Name"]')
    current_name = group_name_input.get_attribute('value')

    if current_name != LOCKED_GROUP_NAME:
        group_name_input.clear()
        group_name_input.send_keys(LOCKED_GROUP_NAME)
        group_name_input.send_keys(Keys.RETURN)  # Submit new name
        print(f'Group name changed back to locked name: {LOCKED_GROUP_NAME}')
    else:
        print('Group name is already locked.')

    time.sleep(2)

def main():
    driver = webdriver.Chrome()  # Or your preferred WebDriver
    try:
        login(driver)
        while True:
            check_and_lock_group_name(driver)
            time.sleep(60)  # Check every 60 seconds
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
