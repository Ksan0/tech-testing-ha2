from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class PageObject(object):
    __site_url = 'https://target.mail.ru'

    def __init__(self, driver=None, page_url='/'):
        self.__driver = driver
        self.__page_url = page_url

    def _find_element(self, by, value, timeout=30, poll_frequency=0.1):
        return WebDriverWait(driver=self.__driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda d: d.find_element(by=by, value=value)
        )

    def _find_element_by_xpath(self, xpath, timeout=30, poll_frequency=0.1):
        return self._find_element(by=By.XPATH, value=xpath, timeout=timeout, poll_frequency=poll_frequency)

    def _find_element_by_id(self, elem_id, timeout=30, poll_frequency=0.1):
        return self._find_element(by=By.ID, value=elem_id, timeout=timeout, poll_frequency=poll_frequency)

    def _find_element_by_class_name(self, elem_class, timeout=30, poll_frequency=0.1):
        return self._find_element(by=By.CLASS_NAME, value=elem_class, timeout=timeout, poll_frequency=poll_frequency)

    def _wait_for(self, l, args, timeout=30, poll_frequency=0.1):
        WebDriverWait(driver=self.__driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda d: l(d, args)
        )

    def open(self):
        self.__driver.get(self.__site_url + self.__page_url)

    def go(self):
        """
        do main action of this page
        action must match the name of class
        """
        raise Exception('need to be overwritten')

    def fill(self, **kwargs):
        """
        fill main part of this page
        """
        raise Exception('need to be overwritten')