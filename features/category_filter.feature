Feature: Category Filter
    As a user
    I want to filter products by category
    So that I can easily find items I want to purchase

    Background:
    Given I navigate to the Home page

    Scenario: Able to see products filtered under the Hammer category when selected
        When I select the Hammer category from the category filter checkbox
        Then I should see products displayed that are under the Hammer category
        And  I unselect the Hammer category from the category filter checkbox
        Then I should see store list restore to default state