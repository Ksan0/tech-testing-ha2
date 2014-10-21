# encoding: utf-8
from pages.PageObject import PageObject


class PageEditCampaign(PageObject):
    def __init__(self, driver):
        super(PageEditCampaign, self).__init__(driver=driver, page_url='/ads/campaigns')

    def open(self):
        raise Exception('unsupported action')

    def open_last_created(self):
        super(PageEditCampaign, self).open()

        edit_xpath = '/html/body/div[1]/div[5]/div[1]/div[2]/div/ul/li[1]/div[2]/div[1]/div[3]/div/ul/li[3]/a'
        edit_elem = self._find_element_by_xpath(xpath=edit_xpath)
        edit_elem.click()

    def get_age_limit(self):
        age_limit_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[7]/div/div[2]/ul/li[3]/div/div[2]/span'
        age_limit_elem = self._find_element_by_xpath(xpath=age_limit_xpath)
        return age_limit_elem.text.replace(u'Не учитывать', 'None')

    def get_interests(self):
        #interests_active_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[7]/div/div[2]/ul/li[21]/div/div[2]/span'
        interests_list_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[7]/div/div[2]/ul/li[21]/div/div[2]/div[2]/div/div/div/ul'

        #interests_active_elem = self._find_element_by_xpath(xpath=interests_active_xpath)
        #interests_active_elem.click()

        interests_list_elem = self._find_element_by_xpath(xpath=interests_list_xpath)
        interests_list = interests_list_elem.find_elements_by_class_name('campaign-setting__chosen-box__item')

        result = [li.get_attribute('data-id') for li in interests_list]

        #interests_active_elem.click()

        return result