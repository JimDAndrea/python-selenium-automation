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
driver.maximize_window()


driver.get('https://www.target.com/')
sleep(4)

# locate the sign in button
driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']").click()
sleep(3)

driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

sleep(3)
actual_result = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
expected_result = 'Sign into your Target account'

assert expected_result in actual_result, f'Expected result not in actual_result'
print ('Test case passed')

driver.quit()