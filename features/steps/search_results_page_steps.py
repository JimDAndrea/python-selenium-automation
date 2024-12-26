from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#not sure if these next 2 lines are needed
from time import sleep
from selenium import webdriver


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_SIDE_NAV_BTN = (By.XPATH, "//button[@data-test='orderPickupButton']")
# ADD_TO_CART_SIDE_NAV_BTN = (By.XPATH, "//button[@data-test='shippingButton']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
LISTINGS = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='productTitle']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[data-test='productImage']")


@given('Open target circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle/')
    # Wait until the Add to Cart button is clickable
    wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN))
    # click element when available
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
    #properly initializing the wait object for the driver
    # wait = WebDriverWait(context.driver, 10)
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_SIDE_NAV_BTN))
    context.driver.find_element(*ADD_TO_CART_SIDE_NAV_BTN).click()

@when("Click on Add to Cart button")
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then ("Verify that every product has a name and an image")
def verify_products_name_img(context):
    context.driver.execute_script("window.scrollBy(0,2000)","")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)","")
    #Find all products:
    all_products = context.driver.find_elements(*LISTINGS)
    # print(all_products)
    assert len(all_products) > 0, 'No products found!'

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title != '', 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)
