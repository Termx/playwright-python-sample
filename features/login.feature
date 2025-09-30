Feature: User Login
  As a registered user,
  I want to log in to my account,
  So that I can access my dashboard.

  Background: Navigate to the Login page
    Given I am on the login page

  Scenario: Successful login with valid credentials
    When I enter valid credentials
    And  I click the login button
    Then I should be redirected to the account page
  
  Scenario: Unsuccessful login with invalid credentials
    When I enter invalid credentials
    And  I click the login button
    Then I should see an error message

  Scenario: Able to see an error message when an email is not provided
    When I enter credentials without an email
    And  I click the login button
    Then I should see the email error message
  
  Scenario: Able to see an error message when a password is not provided
    When I enter credentials without a password
    And  I click the login button
    Then I should see the password error message