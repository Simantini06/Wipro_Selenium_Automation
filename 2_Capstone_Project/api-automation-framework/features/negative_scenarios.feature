Feature: User Management API - Negative Scenarios
  As a QA engineer
  I want to verify the API fails gracefully on bad input
  So that the service behaves predictably under invalid conditions

  Scenario Outline: Verify login fails when a required field is missing
    Given the login request is missing the "<missing_field>" field
    When I send the verify login request
    Then the response code should be 400
    And the response message should be "Bad request, email or password parameter is missing in POST request."

    Examples:
      | missing_field |
      | email         |
      | password      |

  Scenario: Verify login fails for a user that does not exist
    Given a set of credentials that do not belong to any registered user
    When I send the verify login request
    Then the response code should be 404
    And the response message should be "User not found!"
