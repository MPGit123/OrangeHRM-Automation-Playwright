from playwright.sync_api import Page, expect
from config.settings import settings

class BasePage:
    def __init__(self, page:Page):
        self.page = page
        self.page.set_default_timeout(settings.default_timeout_ms)

    def goto(self, utl_text: str):
        self.page.goto(settings.base_url + utl_text)
        self.page.wait_for_load_state(state="networkidle")

    def safe_fill(self, element, text):
        expect(element).to_be_enabled()
        element.fill(text)

    def safe_click(self, element):
        expect(element).to_be_enabled()
        element.click()
        self.page.wait_for_load_state(state="networkidle")