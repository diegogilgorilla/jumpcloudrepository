
Feature: This feature file will contain all tests related to post hash1


  # Shutdown
@second
  Scenario: I want to call POST shutdown service
    Given I call POST shutdown service
    Then the response status code is "200"



