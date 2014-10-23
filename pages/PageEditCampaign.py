# encoding: utf-8
from pages.PageObject import PageObject


class PageEditCampaign(PageObject):
    def __init__(self, driver):
        super(PageEditCampaign, self).__init__(driver=driver, page_url='/ads/campaigns')

    def open(self):
        raise Exception('unsupported action')

    def open_last_created(self):
        super(PageEditCampaign, self).open()

        edit_elem = self._find_element_by_class_name('control__link_edit')
        edit_elem.click()

        l = lambda d, args: self._find_element_by_class_name(args['class_name']).get_attribute('innerHTML') != ''
        self._wait_for(l=l, args={'class_name': 'campaign-setting__chosen-box__body'})

    def get_age_limit(self):
        age_limit_elem = self._find_element_by_class_name('campaign-setting__wrapper_restrict')\
            .find_element_by_class_name('campaign-setting__value')
        return age_limit_elem.text.replace(u'Не учитывать', 'None')

    def get_interests(self):
        interests_list_elem = self._find_element_by_class_name('campaign-setting__wrapper_interests')\
            .find_element_by_class_name('campaign-setting__chosen-box__body')
        interests_list = interests_list_elem.find_elements_by_class_name('campaign-setting__chosen-box__item')

        return [li.get_attribute('data-id') for li in interests_list]