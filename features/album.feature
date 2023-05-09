# Created by ailen.ramayo at 12/1/23
Feature: Albums

  Scenario: Validate GET 200 v1/album
    Given I get the authorization api access token
    When I execute a "GET" request to service "albums" with path variable "valid_album"
    Then I receive a valid "200" status response code

  Scenario: Validate GET 200 v1/albums by market
    Given I get the authorization api access token
    And I get an available market for an album
    When I execute a "GET" request to service "albums" with path variable "valid_album" for an available market
    Then I receive a valid "200" status response code

  Scenario Outline: Validate GET 400 v1/albums invalid request
    Given I get the authorization api access token
    When I execute a "GET" request to service "albums" with path variable "<invalid>"
    Then I receive a valid "400" status response code
    And I receive a valid error message "invalid id"

    Examples: invalid albums ids
      | invalid          |
      | invalid_album_id |
      | empty_album_id   |

  Scenario: Validate GET 401 v1/album unauthorized
    Given I get invalid authorization api access token
    When I execute a "GET" request to service "albums" with path variable "valid_album"
    Then I receive a valid "401" status response code
    And I receive a valid error message "Invalid access token"

#  Scenario: Validate PUT 200 v1/album
#    Given I get the authorization api access token
#    When I execute a "<string>" request to service "<string>" with path variable "<string>"
#    Then I receive a valid "200" status response code