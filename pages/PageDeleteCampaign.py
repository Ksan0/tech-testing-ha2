from pages.PageObject import PageObject


class PageDeleteCampaign(PageObject):
    def __init__(self, driver):
        super(PageDeleteCampaign, self).__init__(driver=driver, page_url='/ads/campaigns/')

    def go(self):
        delete_xpath = '/html/body/div[1]/div[5]/div[1]/div[2]/div/ul/li[1]/div[2]/div[1]/div[3]/div/ul/li[4]/span'
        delete_ypath = '/html/body/div[1]/div[5]/div[1]/div[2]/div/ul/li[1]/div[2]/div[1]/div[3]/div/ul/li[4]/span'
        delete_elem = self._find_element_by_xpath(xpath=delete_xpath)
        delete_elem.click()