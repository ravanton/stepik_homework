from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

import time



class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) 

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"


    # def should_be_browse_store(self):
    #     assert self.is_element_present(*MainPageLocators.BROWSE_STORE), "Browse store link is not presented"

    # def all_products(self):
    #     assert self.is_element_present(*MainPageLocators.ALL_BOOKS), "All books list is not presented"
    #     text = self.browser.find_element(*MainPageLocators.ALL_BOOKS).get_attribute("innerHTML")
    #     all_prod = self.browser.find_element(*MainPageLocators.ALL_BOOKS)
    #     all_prod.click()
    #     page_title = self.browser.find_element(*MainPageLocators.HEADER_ALLBOOKS)
    #     title = page_title.get_attribute("innerHTML")
    #     time.sleep(5)
    #     assert text in title, "ALL PRODUCTS title is not presented"
