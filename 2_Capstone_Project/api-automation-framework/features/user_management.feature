Feature: User Account Management
  As a QA engineer
  I want to automate the full lifecycle of a user account
  So that I can verify the User Management API behaves correctly end-to-end

  Scenario: Successfully manage the full user account lifecycle
    Given I have a new user's registration details
    When I create the user account
    Then the account should be created successfully
    And the response time should be below 3000 ms

    When I verify login with the created user's credentials
    Then the login should be verified successfully

    When I fetch the user detail by email
    Then the returned user detail should match the created user

    When I update the user's account information
    Then the account should be updated successfully

    When I delete the user's account
    Then the account should be deleted successfully
