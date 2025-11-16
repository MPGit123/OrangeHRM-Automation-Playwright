from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext
import pytest
from config.settings import settings

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright:Playwright):
    browser = playwright.chromium.launch(channel=settings.browser, headless=settings.headless, args=["--start-maximized"], slow_mo=settings.slow_mo_ms)
    yield browser
    browser.close()

@pytest.fixture(scope="session")
def context(browser:Browser):
    context = browser.new_context(no_viewport=True)
    yield context
    context.close()

@pytest.fixture()
def page(context:BrowserContext):
    page = context.new_page()
    yield page
    page.close()