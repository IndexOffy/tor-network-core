import logging

from zipfile import ZipFile
from os import system, chmod, path
from urllib.request import urlretrieve, urlopen

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

    try:
        executable_path = ChromeDriverManager().install()
        return webdriver.Chrome(
            executable_path=executable_path,
            chrome_options=chrome_options
        )
    except Exception as error:
        logging.error(error)
        url = "https://chromedriver.storage.googleapis.com/{}/chromedriver_linux64.zip"
        latest_release_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
        file_driver_zip = "./chromedriver_linux64.zip"
        file_driver = "./chromedriver"

        try:
            version = str(urlopen(latest_release_url).read().decode("utf-8"))
        except Exception as error_version:
            logging.error(error)
            version = '108.0.5359.71'

        urlretrieve(url.format(version), file_driver_zip)

        with ZipFile(file_driver_zip, 'r') as zip_ref:
            zip_ref.extractall()
        chmod(file_driver, 0o755)

        return webdriver.Chrome(
            executable_path=file_driver,
            chrome_options=chrome_options
        )


def get_tor_browser(headless: bool = True):
    option = webdriver.FirefoxOptions()
    option.headless = headless

    if not path.exists(FILE_TOR_BROWSER):
        urlretrieve(URL_TOR_BROWSER, FILE_TOR_BROWSER)
        system(f'tar -xvJf {FILE_TOR_BROWSER}')
        system('apt-get install tor')

        get_driver = GetGeckoDriver()
        get_driver.install()

    return TorBrowserDriver('./tor-browser_en-US', options=option)
