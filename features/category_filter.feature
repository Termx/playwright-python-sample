Feature: Category Filter
    Able to filter products by category

    Background:
    Given I navigate to the Home page

    Scenario: Able to see products filtered under the Hammer category when selected
        When I select the Hammer category from the category filter checkbox
        Then I should see products displayed that are under the Hammer category
        And  I unselect the Hammer category from the category filter checkbox
        Then I should see store list restore to default state