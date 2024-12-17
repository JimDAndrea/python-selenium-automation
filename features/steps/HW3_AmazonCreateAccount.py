from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
# Open Amazon.com
driver.get('https://www.amazon.com')
# amazon icon from create account screen
# HW3-Q1-CSS Selector
driver.find_element(By.CSS_SELECTOR,"('div.a-icon a-icon-logo')")
# HW3-Q2
driver.find_element(By.CSS_SELECTOR, "h1,a-spacing-small")
# HW3-Q3
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")
# HW3-Q4
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
HW3-Q5
driver.find_element(By.CSS_SELECTOR, "input#ap_password")
# HW3-Q6
driver.find_element(By.XPATH, "//div[contains(text(), 'Passwords must be at least 6 characters')]")
# HW3-Q7
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
# HW3-Q8
driver.find_element(By.CSS_SELECTOR, "input#Continue")
# HW3-Q9
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']")
# HW3-Q10
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']")
# HW3-Q11
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']")


