Feature: Create Account
    Able to create an account
    
    Background:
        Given I navigate to the Create Account page
    
    Scenario: Able to create a new account
        When I enter the required account details
        Then I should be redirected back to the login page
    
    Scenario: Able to see an error message when the first name is not provided
        When I enter the account details without a first name
        Then I should see the first name error message "First name is required"
    
    Scenario: Able to see an error message when the last name is not provided
        When I enter the account details without a last name
        Then I should see the last name error message "Last name is required"

    Scenario: Able to see an error message when the DOB is not provided or invalid
        When I enter the account details without a DOB
        Then I should see the DOB error message "Date of Birth is required"
        When I enter the account details with an invalid DOB
        Then I should see the invalid DOB error message "Please enter a valid date in YYYY-MM-DD format."

    Scenario: Able to see an error message when the street address is not provided
        When I enter the account details without a street address
        Then I should see the street address error message "Street is required"

    Scenario: Able to see an error message when the postal code is not provided
        When I enter the account details without a postal code
        Then I should see the postal code error message "Postcode is required"

    Scenario: Able to see an error message when the city is not provided
        When I enter the account details without a city
        Then I should see the city error message "City is required"
    
    Scenario: Able to see an error message when the state is not provided
        When I enter the account details without a state
        Then I should see the state error message "State is required"
    
    Scenario: Able to see an error message when the country is not provided
        When I enter the account details without a country
        Then I should see the country error message "Country is required"
    
    Scenario: Able to see an error message when the phone number is not provided or invalid
        When I enter the account details without a phone number
        Then I should see the phone number error message "Phone is required."
        When I enter the account details with an invalid phone number format
        Then I should see the invalid phone number error message "Only numbers are allowed."
    
    Scenario: Able to see an error message when the email is not provided
        When I enter the account details without an email address
        Then I should see the email address error message "Email is required"
    
    # #Password
    Scenario: Able to see an error message when the password is not provided
        When I enter the account details without a password
        Then I should see the password error message "Password is required"
    
    Scenario: Able to see an error message when the password is not 6 characters long
        When I enter the account details with a password less than 6 characters
        Then I should see the minimal password error message "Password must be minimal 6 characters long."
    
    Scenario: Able to see an error message when the password has invalid characters
        When I enter the account details without a password
        Then I should see the invalid password error message "Password can not include invalid characters."

    Scenario: Able to see the password bar graph when the password is weak, moderate, strong, very strong and excellent
        When I enter the account details with a weak password
        Then I should see at least one number requirement has passed
        Then I should see the weak password bar graph of "width: 20%;"
        When I enter the account details with a moderate password
        Then I should see the moderate password bar graph of "width: 40%;"
        When I enter the account details with a strong password
        Then I should see at least one special symbol requirement has passed
        Then I should see the strong password bar graph of "width: 60%;"
        When I enter the account details with a very strong password
        Then I should see both uppercase and lowercase letters requirement have passed
        Then I should see the very strong password bar graph of "width: 80%;"
        When I enter the account details with an excellent password
        Then I should see at least 8 characters long requirement have passed
        Then I should see the excellent password bar graph of "width: 100%;"