from selenium.webdriver.common.by import By
from behave import given, when, then

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.ClickCart()

@then('Click Sign In')
def click_signin(context):
    context.app.header.ClickSignIn()

@then('From right side Navigation menu Click Sign In')
def click_signin_from_nav(context):
    context.app.header.ClickSignInFromNav()

@then('Verify Sign In form opened')
def verify_signin_form(context):
    context.app.header.VerifySignInForm()

@then('Verify at least 1 header link is shown')
def verify_header_links(context):
    el = context.driver.find_element(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind element:')
    print(el)


@then('Verify {expected_amount} header links are shown')
def verify_header_links_amount(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind elements:')
    print(links)
    print(type(len(links)))

    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'