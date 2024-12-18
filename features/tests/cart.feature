Feature: Tests for cart functionality

    Scenario: 'Your cart is empty' message is shown for empty cart
        Given Open target main page
        When Click on Cart icon
        Then Verify 'Your cart is empty' message is shown

    Scenario: User can add a product to cart
        Given Open target main page
        When Search for tea
        And Click on Add to Cart button
        And Confirm Add to Cart button from side navigation
        And Open cart page
        Then Verify cart has 1 item(s)



