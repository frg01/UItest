from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        """导航到Playwright主页"""
        self.page.goto("https://playwright.dev/")

    def click_get_started(self):
        """点击“Get started”链接"""
        self.page.get_by_role("link", name="Get started").click()

    def is_installation_heading_visible(self):
        """验证“Installation”标题是否可见"""
        return self.page.get_by_role("heading", name="Installation").is_visible()

    def search_documentation(self, query: str):
        """在文档中搜索"""
        self.page.fill('input[placeholder="Search"]', query)
        self.page.press('input[placeholder="Search"]', 'Enter')

    def get_title(self):
        """获取当前页面的标题"""
        return self.page.title()
