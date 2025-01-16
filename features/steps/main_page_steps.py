from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()

@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_SIDE_NAV_BTN)).click()
    sleep(4)

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn

@when('Click on Cart icon')
def click_cart(context):
    context.app.header.ClickCart()

@when('Click Sign In')
def click_signin(context):
    context.app.header.ClickSignIn()

@then('From right side Navigation menu Click Sign In')
def click_signin_from_nav(context):
    context.app.header.ClickSignInFromNav()

@when('Input email on SignIn page')
def input_email(context):
    context.app.login_page.InputEmail('******')

@when('Input password on SignIn page')
def input_password(context):
    context.app.login_page.InputPassword('*******')

@then('Verify user is logged in')
def verify_user_logged_in(context):
    context.app.login_page.VerifyUserLoggedIn()

@when('From right side Navigation menu Click Sign In')
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