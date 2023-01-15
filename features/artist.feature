# Created by ailen.ramayo at 12/1/23
Feature: Artist

  Scenario: Validate GET 200 v1/artist artist profile
    Given I get the authorization api access token for execute endpoint "artists"
    When I execute a "GET" request to endpoint path "/artists/" with path variable "valid_artist_id"
    Then I receive a valid "200" status response code
    And The artist "type" should be "artist"
    And The artist "name" should be "Pitbull"

  Scenario: Validate GET 400 v1/artist invalid artist profile
    Given I get the authorization api access token for execute endpoint "artists"
    When I execute a "GET" request to endpoint path "/artists/" with path variable "invalid_artist_id"
    Then I receive a valid "400" status response code
    And I receive a valid error message "invalid id"

  Scenario: Validate GET 400 v1/artist empty artist profile id
    Given I get the authorization api access token for execute endpoint "artists"
    When I execute a "GET" request to endpoint path "/artists/" with path variable "empty_artist_id"
    Then I receive a valid "400" status response code
    And I receive a valid error message "invalid id"
