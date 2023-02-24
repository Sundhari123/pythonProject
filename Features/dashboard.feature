Feature: Dashboard
  @sanity @dashboard
  Scenario: Navigation items present on dashboard
    Given open vdso homepage
    When User in dashboard page
    Then verify all the nav items present on the page