from time import sleep
from selenium.webdriver import *
from pages.PageObject import PageObject


class PageCreateCampaign(PageObject):
    def __init__(self, driver):
        super(PageCreateCampaign, self).__init__(driver=driver, page_url='/ads/create')

    def fill(self, **kwargs):
        """
        :Args:
         - name: campaign name
         - title
         - text
         - url
         - image
        """

        campaign_name_xpath = '/html/body/div[1]/div[5]/div/div[1]/div/div/div[1]/input'
        title_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[2]/input'
        text_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[3]/textarea'
        url_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[4]/span[2]/input'

        campaign_name_elem = self._find_element_by_xpath(xpath=campaign_name_xpath)
        campaign_name_elem.clear()
        campaign_name_elem.send_keys(kwargs['name'])

        title_elem = self._find_element_by_xpath(title_xpath)
        title_elem.send_keys(kwargs['title'])

        text_elem = self._find_element_by_xpath(text_xpath)
        text_elem.send_keys(kwargs['text'])

        url_elem = self._find_element_by_xpath(url_xpath)
        url_elem.send_keys(kwargs['url'])

        image_elem = self._find_element_by_xpath('/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[8]/form/div/input')
        image_elem.send_keys(kwargs['image'])

    def go(self):
        action_elem = self._find_element_by_xpath('/html/body/div[1]/div[5]/div/div[2]/div/div[2]/div[2]/span')
        action_elem.click()

    def wait_for_image_upload(self):
        image_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[8]/span[2]/span[2]'
        self._wait_for_element(xpath=image_xpath)

    def get_preview_data(self):
        edit_xpath = '/html/body/div[1]/div[5]/div[1]/div[2]/div/ul/li/div[2]/div[5]/div/div/div[2]/div[1]/div/ul/li[3]/span'
        campaign_name_xpath = '/html/body/div[1]/div[5]/div[1]/div[2]/div/ul/li/div[1]/div/span[1]'
        title_xpath = '/html/body/div[1]/div[5]/div[1]/div[2]/div/ul/li/div[2]/div[5]/div/div/div[2]/div[3]/div[1]/ul/li[2]/input'
        text_xpath = '/html/body/div[1]/div[5]/div[1]/div[2]/div/ul/li/div[2]/div[5]/div/div/div[2]/div[3]/div[1]/ul/li[3]/textarea'
        url_xpath = '/html/body/div[1]/div[5]/div[1]/div[2]/div/ul/li/div[2]/div[5]/div/div/div[2]/div[3]/div[1]/ul/li[4]/span[2]/input'

        campaign_name_elem = self._find_element_by_xpath(campaign_name_xpath)

        edit_elem = self._find_element_by_xpath(edit_xpath)
        edit_elem.click()

        title_elem = self._find_element_by_xpath(title_xpath)
        text_elem = self._find_element_by_xpath(text_xpath)
        url_elem = self._find_element_by_xpath(url_xpath)

        return {
            'name': campaign_name_elem.text,
            'title': title_elem.text,
            'text': text_elem.text,
            'url': url_elem.text
        }