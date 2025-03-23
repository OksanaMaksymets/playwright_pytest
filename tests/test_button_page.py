import re
from playwright.sync_api import Page, expect
from pages.button_page import ButtonPage

def test_has_title(page: Page):
    button_page = ButtonPage(page)
    button_page.navigate()
    expect(page).to_have_title(re.compile(".*Simple HTML Elements For Automation.*"))

def test_click_click_me_button(page):
    button_page = ButtonPage(page)
    button_page.navigate()
    button_page.click_me_button.click()
    expect(page).to_have_url("https://ultimateqa.com/?")

def test_click_raise_button(page):
    button_page = ButtonPage(page)
    button_page.navigate()
    button_page.raise_button.click()
    expect(page).to_have_url("https://ultimateqa.com/?")
