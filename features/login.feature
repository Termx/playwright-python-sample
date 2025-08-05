Feature: User Login
  As a registered user,
  I want to log in to my account,
  So that I can access my dashboard.

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to the account page
  
  Scenario: Unsuccessful login with invalid credentials
    Given I am on the login page
    When I enter invalid credentials
    And I click the login button
    Then I should see an error message

  Scenario: Able to see an error message when an email is not provided
    Given I am on the login page
    When I enter credentials without an email
    When I click the login button
    Then I should see the email error message
  
  Scenario: Able to see an error message when a password is not provided
    Given I am on the login page
    When I enter credentials without a password
    When I click the login button
    Then I should see the password error message