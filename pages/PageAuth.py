from selenium.webdriver.support.select import Select
from pages.PageObject import PageObject


class PageAuth(PageObject):
    def __init__(self, driver):
        super(PageAuth, self).__init__(driver=driver, page_url='/login')

    def fill(self, **kwargs):
        """
        :Args:
         - login
         - domain
         - password
        """
        login_xpath = '//*[@id="id_Login"]'
        domain_xpath = '//*[@id="id_Domain"]'
        password_xpath = '//*[@id="id_Password"]'

        login_elem = self._find_element_by_xpath(xpath=login_xpath)
        login_elem.send_keys(kwargs['login'])

        domain_elem = self._find_element_by_xpath(xpath=domain_xpath)
        Select(domain_elem).select_by_visible_text(kwargs['domain'])

        pass_elem = self._find_element_by_xpath(xpath=password_xpath)
        pass_elem.send_keys(kwargs['password'])

    def go(self):
        action_xpath = '//*[@id="gogogo"]/input'
        action_elem = self._find_element_by_xpath(action_xpath)
        action_elem.click()

    def get_user_email(self):
        email_xpath = '//*[@id="PH_user-email"]'
        return self._find_element_by_xpath(xpath=email_xpath).text