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
         - title: first banner title
         - text: first banner text
         - url: first banner url
         - image: first banner image
        """

        what_xpath = '//*[@id="product-type-6039"]'
        place_xpath = '//*[@id="pad-mobile_app_web_service"]'

        campaign_name_xpath = '/html/body/div[1]/div[5]/div/div[1]/div/div/div[1]/input'
        title_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[2]/input'
        text_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[3]/textarea'
        url_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[4]/span[2]/input'

        what_elem = self._find_element_by_xpath(xpath=what_xpath)
        what_elem.click()

        place_elem = self._find_element_by_xpath(xpath=place_xpath)
        place_elem.click()

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

    def fill_age_limit(self, limit='None'):
        limit_activate_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[7]/div/div[2]/ul/li[3]/div/div[2]/span'
        limits_xpath = {
            'None': '//*[@id="restrict-"]',
            '0+': '//*[@id="restrict-0+"]',
            '6+': '//*[@id="restrict-6+"]',
            '12+': '//*[@id="restrict-12+"]',
            '16+': '//*[@id="restrict-16+"]',
            '18+': '//*[@id="restrict-18+"]'
        }

        limit_activate_elem = self._find_element_by_xpath(xpath=limit_activate_xpath)
        limit_activate_elem.click()

        limit_elem = self._find_element_by_xpath(xpath=limits_xpath[limit])
        limit_elem.click()

        limit_activate_elem.click()

    def fill_interests(self, root_interest_id, click_interests_id):
        interests_activate_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[7]/div/div[2]/ul/li[21]/div/div[2]/span'
        tree_open_class_name = 'tree__node__collapse-icon'
        input_class_name = 'tree__node__input'

        interests_activate_elem = self._find_element_by_xpath(xpath=interests_activate_xpath)
        interests_activate_elem.click()

        root_interest_elem_li = self._find_element_by_id(elem_id='interests'+root_interest_id)
        root_interest_elem_tree_open = root_interest_elem_li.find_element_by_class_name(tree_open_class_name)
        root_interest_elem_tree_open.click()

        for i_id in click_interests_id:
            elem_li = self._find_element_by_id(elem_id='interests'+i_id)
            elem_input = elem_li.find_element_by_class_name(input_class_name)
            elem_input.click()

        root_interest_elem_tree_open.click()
        interests_activate_elem.click()

    def go(self):
        create_button_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[2]/div[2]/span'
        create_button_elem = self._find_element_by_xpath(xpath=create_button_xpath)
        create_button_elem.click()

    def wait_for_image_upload(self):
        image_xpath = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/span[1]'
        image_elem = self._find_element_by_xpath(xpath=image_xpath)
        l = lambda d, args: args['elem'].get_attribute('style') != 'display: none;'
        self._wait_for(l=l, args={'elem': image_elem})