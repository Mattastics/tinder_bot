import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_driver = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver)
driver.get(url="https://tinder.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="o-1442994379"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()
time.sleep(3)

window_handle_list = driver.window_handles
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)
time.sleep(3)
input_email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("**************")
input_password = driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys("*********")
enter_login = driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()
time.sleep(3)
driver.switch_to.window(base_window)
time.sleep(7)
location = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
time.sleep(7)
notis = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]/span').click()
time.sleep(2)
cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button').click()


for num in range(100):
    time.sleep(4)
    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
    except selenium.common.exceptions.ElementClickInterceptedException:
        try:
            time.sleep(2)
            match_popup = driver.find_element(By.XPATH, '//*[@id="o615757898"]/div/div/div[1]/div/div[3]/button/svg')
            match_popup.click()
        except selenium.common.exceptions.NoSuchElementException:
            no = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/button[2]/span")
