from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)
# Open Amazon.com
driver.get('https://www.amazon.com')
# amazon icon from create account screen
# HW3-Q1-CSS Selector
wait.until(EC.presence_of_element_located((
        By.ESS_SELECTOR, "div.a-icon.a-icon-logo"))
)
driver.find_element(By.CSS_SELECTOR,
                    "i.a-icon.a-icon-logo[role='img'][aria-label='Amazon']")
# HW3-Q2
wait.until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "h1,a-spacing-small"))
)
driver.find_element(By.CSS_SELECTOR, "h1,a-spacing-small")
# HW3-Q3
wait.until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "input#ap_customer_name"))
)
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")
# HW3-Q4
wait.until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "input#ap_email"))
)
driver.find_element(By.CSS_SELECTOR,
                    "input#ap_email")
HW3-Q5
wait.until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "input#ap_password"))
)
driver.find_element(By.CSS_SELECTOR,
                    "input#ap_password")
# HW3-Q6
wait.until(
    EC.presence_of_element_located((
        By.XPATH, "//div[contains(text(), "
                  "'Passwords must be at least 6 characters')]"))
)
wait.until(
    EC.presence_of_element_located(())
)
driver.find_element(By.XPATH,
                    "//div[contains(text(), 'Passwords must be at least 6 characters')]")
# HW3-Q7
wait.until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "input#ap_password_check"))
)
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
# HW3-Q8
wait.until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "input#Continue"))
)
driver.find_element(By.CSS_SELECTOR, "input#Continue")
# HW3-Q9
wait.until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']")
    )
)
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']")
# HW3-Q10
wait.until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']"))
)
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']")
# HW3-Q11
wait.until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']")
    )
)
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']")

driver.quit()
