@first
Feature: This feature file will contain all tests related to post hash


  Scenario: I want to create a hash with alphanumeric password
    Given I call POST hash service with "angrymonkey123" as a "alpha" password
    When the response status code is "200"
    Then service response a number


  Scenario: I want to create a hash with long alphanumeric password
    Given I call POST hash service with "Loremipsumdolorsitamet,acacetsedac suspendisse condimentum, rutrum inceptos viverra velit volutpat ipsum penatibus, fames amet cubilia sit sociis, et tellus maecenas wisi maecenas praesent etiam, adipiscing quis quam at. Dolor et eros posuere, sit nulla dolor enim ornare, diam pellentesque ac turpis facilisis cras lectus. Vitae nullam pellentesque dui aliquam vitae dolor, non congue vel quisque, aliquam donec dui quis et, purus ac varius, velit et amet ipsum in. Dui quam, quisque ut orci. Ut tristique augue tellus nunc elit nunc, augue ut maecenas assumenda vehicula. Amet in in elit pharetra, dictum maecenas maecenas. A hendrerit in ut neque vel elit, faucibus magna ut, sem augue erat et taciti leo, nisl nonummy nibh, amet sed ridiculus in. Dui cras, nunc nulla amet est molestie class, turpis odio ac torquent, molestie consequat commodo." as a "alpha" password
    When the response status code is "200"
    Then service response a number


  Scenario: I want to validate that the hash service only accept string values (json password field as int)
    Given I call POST hash service with "123456789" as a "numeric" password
    Then the response status code is "400"


  Scenario: I want to validate that POST service doesn't accept a null password
    Given I call POST hash service without password
    Then the response status code is "400"


  Scenario: I want to validate the hash service response immediately
    Given I call POST hash service with "testPassword?9" as a "alpha" password
    When the response status code is "200"
    Then service response should response immediately

#get


  Scenario: I want to validate the GET hash service doesn't accept a wrong job identifier
    Given I call GET hash service for "a" as id
    Then the response status code is "400"


  Scenario: I want to validate the GET hash service accept a job identifier
    Given I call GET hash service for "1" as id
    Then the response status code is "200"


  Scenario: I want to validate the hash code is generate as expected
    Given I call POST hash service with "angrymonkey?" as a "alpha" password
    And I call GET hash service
    When the response status code is "200"
    Then validate the hash is right encode

  Scenario: I want to validate the hash code is generate as expected for long password
    Given I call POST hash service with "Loremipsumdolorsitamet,acacetsedac suspendisse condimentum, rutrum inceptos viverra velit volutpat ipsum penatibus, fames amet cubilia sit sociis, et tellus maecenas wisi maecenas praesent etiam, adipiscing quis quam at. Dolor et eros posuere, sit nulla dolor enim ornare, diam pellentesque ac turpis facilisis cras lectus. Vitae nullam pellentesque dui aliquam vitae dolor, non congue vel quisque, aliquam donec dui quis et, purus ac varius, velit et amet ipsum in. Dui quam, quisque ut orci. Ut tristique augue tellus nunc elit nunc, augue ut maecenas assumenda vehicula. Amet in in elit pharetra, dictum maecenas maecenas. A hendrerit in ut neque vel elit, faucibus magna ut, sem augue erat et taciti leo, nisl nonummy nibh, amet sed ridiculus in. Dui cras, nunc nulla amet est molestie class, turpis odio ac torquent, molestie consequat commodo." as a "alpha" password
    And I call GET hash service
    When the response status code is "200"
    Then validate the hash is right encode

 # stats

 Scenario: I want to validate the stats response a valid json
   Given I call GET status service
   When the response status code is "200"
   Then validate the response is a valid json



  Scenario: I want to validate the fields in the stats response
    Given I call POST hash service "1" times
    And I call GET status service
    When the response status code is "200"
    Then validate Total Requests
    And validate Average Time


  Scenario: I want to validate if the stats service doesn't response in POST call
    Given I call POST status service
    When the response status code is "405"


  Scenario: I want to validate if the stats service doesn't response in PUT call
    Given I call PUT status service
    When the response status code is "405"



