# Feature: User Login
#     Verify login features against valid and invalid credentials

#     Background: Navigate to the Login page
#       Given I am on the login page

#     Scenario: Successful login with valid credentials
#       When I enter valid credentials
#       Then I should be redirected to the account page
  
#     Scenario: Unsuccessful login with invalid credentials
#       When I enter invalid credentials
#       Then I should see an error message

#     Scenario: Able to see an error message when an email is not provided
#       When I enter credentials without an email
#       Then I should see the email error message
  
#     Scenario: Able to see an error message when a password is not provided
#       When I enter credentials without a password
#       Then I should see the password error message

#     Scenario: Able to request a password reset
#       When I request a password reset
#       Then I should see a password reset confirmation message
  
#     Scenario: Unable to request a password reset with an invalid email
#       When I request a password reset with an invalid email
#       Then I should see password reset field display an invalid error message
  
#     Scenario: Unable to request a password reset without an email address
#       When I request a password reset without an email address
#       Then I should see password reset field display an error message