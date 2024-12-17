from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target help page')
def open_main(context):
    context.driver.get('http://www.target.com/')
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)
    context.driver.find_element(By.XPATH, "//div[@aria-label='Target Help']").click()
    sleep(5)
    context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Target Help')]")
    context.driver.find_element(By.XPATH, "//input[@id='j_id0:j_id2:j_id32:name']")
    context.driver.find_element(By.CSS_SELECTOR, "input[src='/help/resource/1670947405000/help_search_icon']")
    context.driver.find_element(By.CSS_SELECTOR, 'div.container.clearfix')
    context.driver.find_element(By.CSS_SELECTOR, 'div.col-lg-12')
    context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Browse all Help pages')]")
    sleep(5)

#    context.driver.find_element(By.CSS_SELECTOR, "div[aria-label='Target Help']")
#  $$("[data-test='@web/component-footer/PrimaryFooter']")
#  context.driver.find_element(By.XPATH, "a[href='https://help.target.com/help']").click()
    sleep(3)




# @then('Verify Interface Links')
# def verify_interface_links(context):
#     el = context.driver.find_element(By.CSS_SELECTOR, "[h2[@class='custom-h2']")
#     print('\nFind element:')
#     print(el)

