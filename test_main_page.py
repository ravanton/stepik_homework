from .pages.login_page import LoginPage

from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.locators import ProductPageLocators

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()





# class TestBrowseStore():
#     def test_all_products(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/"
#         page = MainPage(browser, link)
#         page.open()
#         page.should_be_browse_store()
#         page.all_products()

# def test_guest_cant_see_success_message(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     item_page = ProductPage(browser, link)
#     item_page.open()
#     item_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     item_page = ProductPage(browser, link)
#     item_page.open()
#     item_page.add_to_basket()
#     item_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     item_page = ProductPage(browser, link)
#     item_page.open()
#     item_page.add_to_basket()
#     item_page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     page.should_be_login_link()


class TestLoginFromMainPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()