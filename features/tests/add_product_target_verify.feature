# Created by james at 12/9/2024
Feature: Add product to cart and verify cart
  # use main_page_steps.py to open main page and search_results_page_steps.py to click add to cart and verify item is in cart
Scenario: 'Your cart is empty' message is shown for empty cart
  Given Open target main page
  When Click on Cart icon
  Then Verify 'Your cart is empty' message is shown

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for notebook
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then  Verify cart has 1 item(s)

