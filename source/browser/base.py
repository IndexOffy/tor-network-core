from os import system
from os.path import exists
from urllib.request import urlretrieve

from selenium import webdriver
from get_gecko_driver import GetGeckoDriver
from tbselenium.tbdriver import TorBrowserDriver
from webdriver_manager.chrome import ChromeDriverManager
from settings import URL_TOR_BROWSER, FILE_TOR_BROWSER


def get_chrome_browser(headless: bool = True):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    if headless:
        chrome_options.add_argument("--headless")
    
    executable_path = ChromeDriverManager().install()
    return webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)


def get_tor_browser(headless: bool = True):
    option = webdriver.FirefoxOptions()
    option.headless = headless

    if not exists(FILE_TOR_BROWSER):
        urlretrieve(URL_TOR_BROWSER, FILE_TOR_BROWSER)
        system(f'tar -xvJf {FILE_TOR_BROWSER}')
        system('apt-get install tor')

        get_driver = GetGeckoDriver()
        get_driver.install()

    return TorBrowserDriver('./tor-browser_en-US', options=option)
