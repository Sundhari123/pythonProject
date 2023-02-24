from behave import *
from Locators import locatorsForLogin
from Helper.SeleniumHelper import SeleniumHelper
from TestData import testData


@given(u'open vdso homepage')
def openHomepage(context):
    SeleniumHelper(context.driver).open_page(testData.login_url)
    SeleniumHelper(context.driver).wait_till_element_is_present(locatorsForLogin.input_field_login)
    SeleniumHelper(context.driver).insert_text_in_input_field(locatorsForLogin.input_field_login, testData.login_id)
    SeleniumHelper(context.driver).insert_text_in_input_field(locatorsForLogin.input_field_password, testData.login_password)
    SeleniumHelper(context.driver).click(locatorsForLogin.button_login)


@when(u'User in dashboard page')
def userInDashboardPage(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(locatorsForLogin.dashboard_profile_icon)



@then(u'verify all the nav items present on the page')
def verifyNavItems(context):
    url = context.driver.current_url
    assert url == "https://vdso-staging.prodapt.io/dashboard"
