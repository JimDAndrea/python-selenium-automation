 # Created by lana at 12/5/24
Feature: Tests for Main page UI

  Scenario: User can see header links
    Given Open target main page
    Then Verify at least 1 header link is shown
    And Click Sign In
    Then From right side Navigation menu Click Sign In
    Then Verify Sign In form opened

  Scenario: User can see correct amount of header links
    Given Open target main page
    Then Verify 6 header links are shown
