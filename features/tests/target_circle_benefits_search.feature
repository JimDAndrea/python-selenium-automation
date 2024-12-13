# Created by james at 12/9/2024
Feature: Verify there are 14 benefit cells on page
  # Enter feature description here

  Scenario: Check www.target.com/circle page for 14 benefit cells
    Given Open target circle page
    When benefit cells are located
    Then verify number of cells

