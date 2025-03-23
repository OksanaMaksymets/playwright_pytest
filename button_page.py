from playwright.sync_api import Page

class ButtonPage:
    def __init__(self, page: Page):
        self.page = page
        self.click_me_button = page.get_by_role('button', name='Click Me!')
        self.raise_button = page.get_by_role('button', name='Raise')

    def navigate(self):
        self.page.goto("https://ultimateqa.com/simple-html-elements-for-automation/")
