import re ,pytest_playwright,pytest
from playwright.sync_api import Page, expect,sync_playwright
from ..service.NavigateService import NavigateService



class TestHomePage: 
    
    def setup_class(self):
     pass
    
    def teardown_class(self):
        pass   
    
    def setup_method(self):
        pass
    
    def teardown_method(self):
        pass
    
    @pytest.fixture(scope="session")
    def browser(self, playwright):
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()
    
    @pytest.fixture(scope="session")
    def page(self, browser):
        page = browser.new_page()
        yield page
        browser.close()
    
   
    def test_goto_home_page(self, page):
          navigate_service = NavigateService(page)
          navigate_service = NavigateService(page)
          navigate_service.goto_home_page()
          assert True





