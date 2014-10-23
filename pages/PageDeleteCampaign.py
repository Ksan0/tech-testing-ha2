# encoding: utf-8
from pages.PageObject import PageObject


class PageDeleteCampaign(PageObject):
    def __init__(self, driver):
        super(PageDeleteCampaign, self).__init__(driver=driver, page_url='/ads/campaigns/')

    def go(self):
        campaign_elem = self._find_element_by_class_name('campaign-row')

        l = lambda d, args: args['elem'].find_element_by_class_name('control__preset_delete')
        self._wait_for(l=l, args={'elem': campaign_elem})

        delete_elem = campaign_elem.find_element_by_class_name('control__preset_delete')
        delete_elem.click()

        l = lambda d, args: args['elem'].find_element_by_class_name('control__status_campaign').text != u'Удалена'
        self._wait_for(l=l, args={'elem': campaign_elem})