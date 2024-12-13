from playwright.sync_api import Page

class DocPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://playwright.dev/python/docs/intro")

