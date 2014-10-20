from selenium.webdriver.support.wait import WebDriverWait


class PageObject(object):
    __site_url = 'https://target.mail.ru'

    def __init__(self, driver=None, page_url='/'):
        self.__driver = driver
        self.__page_url = page_url

    def _find_element_by_xpath(self, xpath, timeout=30, poll_frequency=0.1):
        return WebDriverWait(driver=self.__driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda d: d.find_element_by_xpath(xpath)
        )

    def _wait_for_element(self, xpath, timeout=30, poll_frequency=0.1):
        self._find_element_by_xpath(xpath=xpath, timeout=timeout, poll_frequency=poll_frequency)

    def open(self):
        self.__driver.get(self.__site_url + self.__page_url)

    def fill(self, **kwargs):
        raise Exception('need to be overwritten')

    def go(self):
        raise Exception('need to be overwritten')