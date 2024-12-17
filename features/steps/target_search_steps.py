from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click cart from main page')
def click_cart(context):
    context.driver.find_element(By.XPATH,"//use[@href='/icons/Cart.svg#Cart']").click()
    sleep(5)


@then('Verify Your cart is empty')
def verify_empty_cart(context):
    #verify cart is empty
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h3[contains(text(), 'Your Amazon Cart is empty')]")
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
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

