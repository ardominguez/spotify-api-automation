# Created by ailen.ramayo at 12/1/23
Feature: Albums

  Scenario: Validate GET 200 v1/album
    Given I get the authorization api access token for execute endpoint "albums"
    When I execute a "GET" request to endpoint path "/albums/" with path variable "valid_album_id"
    Then I receive a valid "200" status response code

  Scenario: Validate GET 200 v1/albums by market
    Given I get the authorization api access token for execute endpoint "albums"
    And I get an available market for an album
    When I execute a "GET" request to "/albums/" with path variable "valid_album_id" for an available market
    Then I receive a valid "200" status response code

  Scenario: Validate GET 400 v1/artist invalid artist profile
    Given I get the authorization api access token for execute endpoint "albums"
    When I execute a "GET" request to endpoint path "/albums/" with path variable "invalid_album_id"
    Then I receive a valid "400" status response code
    And I receive a valid error message "invalid id"

  Scenario: Validate GET 400 v1/artist empty artist profile id
    Given I get the authorization api access token for execute endpoint "albums"
    When I execute a "GET" request to endpoint path "/albums/" with path variable "empty_album_id"
    Then I receive a valid "400" status response code
    And I receive a valid error message "invalid id"