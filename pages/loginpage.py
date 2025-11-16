from playwright.sync_api import Page
from pages.basepage import BasePage
from pages.dashbaordpage import DashboardPage
from config.settings import settings

class LogInPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.usernameBox = page.get_by_role("textbox", name="username")
        self.passwordBox = page.get_by_role("textbox", name="password")
        self.loginButton = page.get_by_role("button", name="Login")
        self.dashboardPage = DashboardPage(page)

    def open_orange_hrm(self):
        self.goto("web/index.php/auth/login")

    def perform_login(self):
        self.safe_fill(self.usernameBox, settings.username)
        self.safe_fill(self.passwordBox, settings.password)
        self.safe_click(self.loginButton)
        return self.dashboardPage