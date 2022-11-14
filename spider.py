# coding=utf-8

"""
Source Base
"""

__all__ = ['BaseSource']


from selenium import webdriver
from requests_html import HTMLSession
from webdriver_manager.chrome import ChromeDriverManager


class BaseSource(object):
    """Base class for data scraping
    """

    def __init__(self):
        """Constructor
        """
        self.session = HTMLSession()
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
