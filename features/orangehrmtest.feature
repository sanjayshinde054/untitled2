Feature: OrangeHRM Login

  Scenario: login to OrangeHRm with valid parameters
    Given launch chrome browser
    When open orangehrm homepage
    And  Enter username "admin" and password "admin123"
    And click on login button
    Then user must successfully login to the dashboard
    And close browser

