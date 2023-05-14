import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def follow_female_followers(username, password, url):
    # Initialize Chrome webdriver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Navigate to the Instagram login page
    driver.get("https://www.instagram.com/accounts/login/")

    # Wait for the page to load
    time.sleep(3)

    # Fill in the login details and submit the form
    try:
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
    except:
        print("Could not login to Instagram")

    # Wait for the login process to complete
    time.sleep(5)

    # Navigate to the Instagram profile URL
    driver.execute_script("window.open('{}','_self',scrollbars=1);".format(url))

    # Wait for the page to load
    time.sleep(5)

    # Click the followers button to view the list of followers
    followers_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/{}/followers/"]'.format(username))))
    followers_button.click()

    # Wait for the list of followers to load
    time.sleep(5)

    # Scroll down the followers list to load more followers
    followers_list = driver.find_element_by_xpath('//div[@role="dialog"]//ul')
    last_height = driver.execute_script("return arguments[0].scrollHeight", followers_list)
    while True:
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", followers_list)
        time.sleep(2)
        new_height = driver.execute_script("return arguments[0].scrollHeight", followers_list)
        if new_height == last_height:
            break
        last_height = new_height

    # Get all the follower buttons on the page
    follower_buttons = driver.find_elements_by_xpath('//button[contains(text(),"Follow")]')

    # Click all the follower buttons that belong to female followers
    for button in follower_buttons:
        follower_name = button.find_element_by_xpath('..//..//div[2]/div[1]').text
        first_name = follower_name.split()[0]
        female_suffixes = ['a', 'aa', 'i', 'ka', 'mi', 'ta']
        for suffix in female_suffixes:
            if first_name.endswith(suffix):
                button.click()
                time.sleep(1)
                break

    # Close the followers list and the browser
    close_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]//button')))
    close_button.click()
    time.sleep(1)
    driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Follow followers script')
    parser.add_argument('username', help='Your username')
    parser.add_argument('password', help='Your password')
    parser.add_argument('url', help='The URL of the page to follow its followers')
    args = parser.parse_args()
    follow_female_followers(args.username, args.password, args.url)
