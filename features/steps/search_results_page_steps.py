from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_SIDE_NAV_BTN = (By.XPATH, "//button[@data-test='orderPickupButton']")
# ADD_TO_CART_SIDE_NAV_BTN = (By.XPATH, "//button[@data-test='shippingButton']")


@given('Open target circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle/')


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    sleep(3)
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected text {product} not in actual {actual_result}'


@then('verify number of cells')
def verify_number_of_cells(context):
    assert len(context.benefit_cells) == 14, f"Expected 14 benefit cells, but found {len(context.benefit_cells)}."


@when('benefit cells are located')
def benefit_cells_located(context):
    context.benefit_cells = context.driver.find_elements(By.CSS_SELECTOR,'.cell-item-content')


@when('Verify item is in cart')
def verify_item_in_cart(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span.h-text-lg').text
    assert product in actual_result, f'Expected text "Added to cart" not in actual {actual_result}'

@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    sleep(3)
    context.driver.find_element(*ADD_TO_CART_SIDE_NAV_BTN).click()
    sleep(4)




