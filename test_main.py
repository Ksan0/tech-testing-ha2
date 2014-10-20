import unittest
from selenium.webdriver import *
from pages.PageAuth import PageAuth
from pages.PageCreateCampaign import PageCreateCampaign


class FuncTestCase(unittest.TestCase):
    def setUp(self):
        driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME.copy()
        )

        page_auth = PageAuth(driver)
        page_auth.open()
        page_auth.fill(login='tech-testing-ha2-6', domain='@bk.ru', password='Pa$$w0rD-6')
        page_auth.go()

        self.__driver = driver
        self.current_page = page_auth

    def tearDown(self):
        #self.__driver.close()
        pass

    #def test_auth(self):
    #    self.assertEqual(self.current_page.get_user_email(), 'tech-testing-ha2-6@bk.ru')

    def test_create_campaign(self):
        page_create_campaign = PageCreateCampaign(self.__driver)
        page_create_campaign.open()
        page_create_campaign.fill(name='rrr', title='qqq', text='www', url='tech.ru', image='/home/ksan0/TP/QA/tech-testing-ha2/image.jpg')
        page_create_campaign.wait_for_image_upload()
        page_create_campaign.go()

        preview_data = page_create_campaign.get_preview_data()
        self.assertEqual(preview_data['name'], 'rrr')
        self.assertEqual(preview_data['title'], 'qqq')
        self.assertEqual(preview_data['text'], 'www')
        self.assertEqual(preview_data['url'], 'tech.ru')

