from playwright.sync_api import Page
from pages.basepage import BasePage
from playwright.sync_api import expect

class DashboardPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.topBarHeader = page.locator(".oxd-topbar-header-title")

    def top_header(self):
        return self.topBarHeader