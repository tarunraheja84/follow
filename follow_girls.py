from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time

# Set username and password
username = "aryantuteja1234"
password = "abc@abc"

# Initialize Chrome webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the Instagram login page
url = "https://www.instagram.com/accounts/login/"
driver.get(url)

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
url = "https://www.instagram.com/connectatpiet/following"
driver.get(url)

# Wait for the page to load
time.sleep(3)

# Scroll down the followers list to load more followers


prev_span_tags=set()
st=set()
prev_size=len(st)
while True:
    span_tags = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.xo1l8bm.x1roi4f4.x10wh9bi.x1wdrske.x8viiok.x18hxmgj > span.x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft')))
    
    followers=set()
    for tag in span_tags:
        if tag not in prev_span_tags:
          followers.add(tag)

    temp=set()
    for tag in followers:
        temp.add(tag)
    
    for tag in prev_span_tags:
        st.add(tag)

    for tag in temp:
        if tag in st:
          followers.remove(tag)
    
    

    prev_span_tags=followers
    curr_size=len(st)
    if(curr_size==prev_size and curr_size>0):
        print(f"{curr_size} followers scanned.")
        driver.quit()
        driver.close()
    prev_size=curr_size
   # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Move the mouse to the center of the screen
    pyautogui.moveTo(screen_width / 2, screen_height / 2)


    # Scroll downwards
    pyautogui.scroll(-1500)  # The negative sign indicates scrolling downwards
    time.sleep(2)

    # Define a list of suffixes that indicate a female name
    female_suffixes = ['a', 'i', 'A', 'I']

    try:
        for follower in followers:
            first_name = follower.text.split()[0]
            # followers_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "followers_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'x9f619') and contains(@class, 'x1n2onr6') and contains(@class, 'x1ja2u2z') and contains(@class, 'x78zum5') and contains(@class, 'x1iyjqo2') and contains(@class, 'xs83m0k') and contains(@class, 'xeuugli') and contains(@class, 'x1qughib') and contains(@class, 'x6s0dn4') and contains(@class, 'x1a02dak') and contains(@class, 'x1q0g3np') and contains(@class, 'xdl72j9')]/span[contains(@class, 'x1lliihq') and contains(@class, 'x193iq5w') and contains(@class, 'x6ikm8r') and contains(@class, 'x10wlt62') and contains(@class, 'xlyipyv') and contains(@class, 'xuxw1ft') and contains(text(), '{}')]/following-sibling::div[contains(@class, 'x9f619') and contains(@class, 'x1n2onr6')']".format(follower.text))))
            # followers_button = WebDriverWait(driver, 10).until(
            # EC.presence_of_element_located((
            #     By.XPATH, 
            #     "//div[contains(@class, 'x9f619') and contains(@class, 'x1n2onr6') and contains(@class, 'x1ja2u2z') and contains(@class, 'x78zum5') and contains(@class, 'x1iyjqo2') and contains(@class, 'xs83m0k') and contains(@class, 'xeuugli') and contains(@class, 'x1qughib') and contains(@class, 'x6s0dn4') and contains(@class, 'x1a02dak') and contains(@class, 'x1q0g3np') and contains(@class, 'xdl72j9')]/span[contains(@class, 'x1lliihq') and contains(@class, 'x193iq5w') and contains(@class, 'x6ikm8r') and contains(@class, 'x10wlt62') and contains(@class, 'xlyipyv') and contains(@class, 'xuxw1ft') and contains(text(), {})]/following-sibling::div[contains(@class, 'x9f619') and contains(@class, 'x1n2onr6')]".format(follower.text)
            # )))

            for suffix in female_suffixes:
                if first_name.endswith(suffix):
                    # followers_button.click()
                    print(first_name)
                    break
    except:
        pyautogui.scroll(-1500)  # The negative sign indicates scrolling downwards
        time.sleep(2)

    while(prev_span_tags==followers):
        followers = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.xo1l8bm.x1roi4f4.x10wh9bi.x1wdrske.x8viiok.x18hxmgj > span.x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft')))
        pyautogui.scroll(-1500)  # The negative sign indicates scrolling downwards
        time.sleep(2)
        # print(prev_span_tags==followers)
    




