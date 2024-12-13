from playwright.sync_api import Page
from ..page.HomePage import HomePage


class NavigateService:
    def __init__(self, page: Page):
        self.home_page = HomePage(page)

    def goto_home_page(self):   
        self.home_page.navigate()
        self.home_page.click_get_started()
        # 确保页面加载完成
        self.home_page.page.wait_for_load_state("networkidle")
        assert self.home_page.is_installation_heading_visible()



