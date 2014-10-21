#!/usr/bin/env python2
import unittest
from selenium import webdriver
from FuncTestCase import FuncTestCase


def main():
    # driver = webdriver.Chrome('/home/ksan0/TP/QA/chromedriver')
    # driver.get("http://ya.ru/")
    suite = unittest.TestSuite((unittest.makeSuite(FuncTestCase), ))
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    main()
