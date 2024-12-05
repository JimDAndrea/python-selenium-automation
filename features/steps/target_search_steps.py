from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click cart from main page')
def click_cart(context):
    context.driver.find_element(By.XPATH,"//use[@href='/icons/Cart.svg#Cart']").click()
    sleep(5)

@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@then('Verify Your cart is empty')
def verify_empty_cart(context):
    #verify signin page exists
    context.driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 fJliSz']").click()
    sleep(5)


@when('Click signin from main page')
def click_signin(context):
    context.driver.find_element(By.XPATH,"//span[@class='sc-58ad44c0-3 kkWqdY h-margin-r-x3' and text()='Sign in']").click()
    sleep(5)

@when('Click signin from sidebar')
def click_sidebar_signin(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='accountNav-signIn']")


@then('Verify signin form opened')
def verify_signin_form(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']")
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
    sleep(5)


@then('Verify search results shown')
def verify_search_results(context):
    expected_result = 'tea'
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
    print('Test case passed')

