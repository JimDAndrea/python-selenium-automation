from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    #modified for 91511634
    expected_colors = ['dark khaki', 'grey', 'navy/tan', 'white/sand/tan']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()
        sleep(2)
        #removed .text as this was not callable and getting errors
        selected_color = context.driver.find_elements(*SELECTED_COLOR)[2].text
#removed .split from selected_color.split('\n')[1]
        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        #added 3 lines to check for out of stock
        if "Out of Stock" in selected_color:
            print(f"Skipping out-of-stock color: {selected_color}")
            continue
        else:
            print(f"Selected color: {selected_color}")
            print('Current color', selected_color)
            actual_colors.append(selected_color)
            print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'