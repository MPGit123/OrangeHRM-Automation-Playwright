from pages.loginpage import LogInPage
from playwright.sync_api import expect

def test_login(page):
    loginPage = LogInPage(page)
    loginPage.open_orange_hrm()
    dashboardPage = loginPage.perform_login()
    expect(dashboardPage.topBarHeader).to_be_visible()