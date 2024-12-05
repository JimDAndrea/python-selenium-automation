Feature: Tests for search

  Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify search results shown

#HW3-Question2
  Scenario: Click Cart icon on open target page to verify it is empty
    Given Open target main page
    When Click cart from main page
    Then Verify Your cart is empty

#    HW3-Question3
#    2) open target and click on cart icon -
#    verify your cart is empty
#    Then Verify search results shown for coffee

  Scenario: Logged out user navigate to sign in
    Given Open target main page
    When Click signin from main page
    When Click signin from sidebar
    Then Verify signin form opened
