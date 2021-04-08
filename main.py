"""
AUTHOR: ENRICO PERSICO, 2021

Displays number of posts, amount of followers, and people following the user
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

username = "YOUR INSTAGRAM USERNAME"
password = "YOUR INSTAGRAM PASSWORD"
time_between_clicks = 0.5
user_agent = "YOUR USER AGENT, IF YOU DON'T KNOW WHAT IT IS, VISIT https://www.whatismybrowser.com/detect/what-is-my-user-agent"
profile = 'USERNAME OF THE PROFILE YOU WANT TO SCRAPE'

# web driver configuration
optns = Options()
optns.add_argument(f"user-agent=[{user_agent}]")
optns.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=optns)
# logs in to Insta
driver.get('https://www.instagram.com')
time.sleep(time_between_clicks)
username_field = driver.find_element_by_xpath("//input[@name='username']")
password_field = driver.find_element_by_xpath("//input[@name='password']")
time.sleep(time_between_clicks)
username_field.send_keys(username)
time.sleep(time_between_clicks)
password_field.send_keys(password)
submit_btn = driver.find_element_by_xpath("//button[@type='submit']")
time.sleep(time_between_clicks)
submit_btn.click()
time.sleep(3)

# goes to profile
driver.get('https://www.instagram.com/' + profile + '/')

profile_info = driver.find_elements_by_xpath("//span[@class = 'g47SY ']")
# prints profile information
print('\n')
print("Posts: " + profile_info[0].text)
print("Follower Count: " + profile_info[1].text)
print("Following Count: " + profile_info[2].text)
print('\n')

# closes web driver
driver.close()
