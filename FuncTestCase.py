import unittest
from selenium.webdriver import *
from pages.PageAuth import PageAuth
from pages.PageCreateCampaign import PageCreateCampaign
from pages.PageDeleteCampaign import PageDeleteCampaign
from pages.PageEditCampaign import PageEditCampaign
import os

# 105: all, 106-110: parts


class FuncTestCase(unittest.TestCase):
    def setUp(self):
        self.auth_fill_args = {
            'login': 'tech-testing-ha2-6',
            'domain': '@bk.ru',
            'password': os.environ['TTHA2PASSWORD']
        }
        self.__base_fill_args = {
            'name': 'new company',
            'title': 'title',
            'text': 'text',
            'url': 'https://play.google.com/store/apps/details?id=com.android.chrome&hl=ru',
            'image': '/home/ksan/TP/Quality/tech-testing-ha2/image.jpg'
        }

        driver = eval(
        "Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.{0}.copy())"
        .format(os.environ['TTHA2BROWSER'])
        )

        page_auth = PageAuth(driver)
        page_auth.open()
        page_auth.fill(**self.auth_fill_args)
        page_auth.go()

        self.__driver = driver
        self.current_page = page_auth

    def __create_campaign_base(self):
        page = PageCreateCampaign(self.__driver)
        page.open()
        page.fill(**self.__base_fill_args)
        page.wait_for_image_upload()
        return page

    def __remove_campaign_base(self):
        page_del = PageDeleteCampaign(self.__driver)
        page_del.open()
        page_del.go()

    def __cleanup_close_window(self):
        self.__driver.quit()

    def __cleanup_remove_page_and_close_window(self):
        self.__remove_campaign_base()
        self.__cleanup_close_window()

    def test_auth(self):
        self.assertEqual(self.current_page.get_user_email(), self.auth_fill_args['login'] + self.auth_fill_args['domain'])
        self.current_page = None
        self.addCleanup(self.__cleanup_close_window)

    def test_create_campaign_empty(self):
        self.current_page = None

        page = self.__create_campaign_base()
        self.addCleanup(self.__cleanup_remove_page_and_close_window)
        page.go()

        page = PageEditCampaign(self.__driver)
        page.open_last_created()
        self.assertEqual('None', page.get_age_limit())
        self.assertEqual([], page.get_interests())

    def test_create_campaign_full(self):
        self.current_page = None

        age_limit = '18+'
        click_interests_id = ['106', '107', '108', '109', '110']

        page = self.__create_campaign_base()
        self.addCleanup(self.__cleanup_remove_page_and_close_window)
        page.fill_age_limit(age_limit)
        page.fill_interests(root_interest_id='105', click_interests_id=click_interests_id)
        page.go()

        page = PageEditCampaign(self.__driver)
        page.open_last_created()
        self.assertEqual(age_limit, page.get_age_limit())
        self.assertEqual(['105'], page.get_interests())

    def test_create_campaign_part(self):
        self.current_page = None

        age_limit = '0+'
        click_interests_id = ['106', '108', '110']

        page = self.__create_campaign_base()
        self.addCleanup(self.__cleanup_remove_page_and_close_window)
        page.fill_age_limit(age_limit)
        page.fill_interests(root_interest_id='105', click_interests_id=click_interests_id)
        page.go()

        page = PageEditCampaign(self.__driver)
        page.open_last_created()
        self.assertEqual(age_limit, page.get_age_limit())
        self.assertEqual(click_interests_id, page.get_interests())
