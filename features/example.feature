Feature: Playwright and Behave integration
  Scenario: Open Playwright homepage
    Given I launch the browser
    When I go to "https://playwright.dev"
    Then the page title should contain "Playwright"
