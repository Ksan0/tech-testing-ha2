from time import sleep
from selenium.webdriver import *
from pages.PageObject import PageObject


class PageCreateCampaign(PageObject):
    def __init__(self, driver):
        super(PageCreateCampaign, self).__init__(driver=driver, page_url='/ads/create')

    def fill(self, **kwargs):
        """
        :Args:
         - title: first banner title
         - text: first banner text
         - url: first banner url
         - image: first banner image
        """

        what_xpath = '//*[@id="product-type-6039"]'
        place_xpath = '//*[@id="pad-mobile_app_web_service"]'

        what_elem = self._find_element_by_xpath(xpath=what_xpath)
        what_elem.click()

        place_elem = self._find_element_by_xpath(xpath=place_xpath)
        place_elem.click()

        li_form_list = self._find_element_by_class_name(elem_class="banner-form__list").find_elements_by_class_name("banner-form__row")
        l_find_input_by_data_name = lambda _list, _data_name, _index=0: [x for x in _list if x.get_attribute('data-name') == _data_name][_index]\
            .find_element_by_class_name('banner-form__input')

        title_elem = l_find_input_by_data_name(li_form_list, 'title')
        title_elem.send_keys(kwargs['title'])

        text_elem = l_find_input_by_data_name(li_form_list, 'text')
        text_elem.send_keys(kwargs['text'])

        url_elem = l_find_input_by_data_name(li_form_list, 'url', 1)
        url_elem.send_keys(kwargs['url'])

        image_elem = l_find_input_by_data_name(li_form_list, 'image')
        image_elem.send_keys(kwargs['image'])

    def fill_age_limit(self, limit='None'):
        limits_xpath = {
            'None': '//*[@id="restrict-"]',
            '0+': '//*[@id="restrict-0+"]',
            '6+': '//*[@id="restrict-6+"]',
            '12+': '//*[@id="restrict-12+"]',
            '16+': '//*[@id="restrict-16+"]',
            '18+': '//*[@id="restrict-18+"]'
        }

        limit_activate_elem = self._find_element_by_class_name('campaign-setting__wrapper_restrict')\
            .find_element_by_class_name('campaign-setting__value')
        limit_activate_elem.click()

        limit_elem = self._find_element_by_xpath(xpath=limits_xpath[limit])
        limit_elem.click()

        limit_activate_elem.click()

    def fill_interests(self, root_interest_id, click_interests_id):
        tree_open_class_name = 'tree__node__collapse-icon'
        input_class_name = 'tree__node__input'

        interests_activate_elem = self._find_element_by_class_name('campaign-setting__wrapper_interests')\
            .find_element_by_class_name('campaign-setting__value')
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
        create_button_elem = self._find_element_by_class_name('main-button-new')
        create_button_elem.click()

    def wait_for_image_upload(self):
        image_elem = self._find_element_by_class_name('banner-preview__img')
        l = lambda d, args: args['elem'].get_attribute('style') != 'display: none;'
        self._wait_for(l=l, args={'elem': image_elem})