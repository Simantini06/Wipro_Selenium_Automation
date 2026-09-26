Feature: Framework reusability across a second API
  As a QA lead
  I want the same client/config/reporting design to work against another API
  So that the framework is proven reusable, not hardcoded to one service

  Scenario: Fetch a user from JSONPlaceholder using the same framework
    When I fetch user 2 from JSONPlaceholder
    Then the JSONPlaceholder response should match the user schema
