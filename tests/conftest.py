import pytest
from playwright.sync_api import Playwright, sync_playwright, Browser

@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    """Ініціалізує Playwright один раз на всю сесію тестів"""
    p = sync_playwright().start()
    yield p
    p.stop()

@pytest.fixture
def browser(playwright_instance) -> Browser:
    """Запускає окремий браузер для кожного тесту, щоб уникнути конфліктів"""
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    """Створює нову сторінку для кожного тесту"""
    page = browser.new_page()
    yield page
    page.close()