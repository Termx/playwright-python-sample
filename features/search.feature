Feature: Search
    Able to search for prodcuts

    Background:
        Given I navigate to the Home page

    Scenario: Able to see search results when a valid product name is entered
        When I enter a valid product name in the search bar
        Then I should see the Thor search results display
        And  I click the X button to clear the search results
        Then I should see store list restore to default state