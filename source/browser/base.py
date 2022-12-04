import logging

from os import system, chmod, path
from urllib.request import urlretrieve, urlopen
from zipfile import ZipFile

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from get_gecko_driver import GetGeckoDriver
from tbselenium.tbdriver import TorBrowserDriver
from webdriver_manager.chrome import ChromeDriverManager

from settings import URL_TOR_BROWSER, FILE_TOR_BROWSER


def run_binary_path_chrome(options):
    url = "https://chromedriver.storage.googleapis.com/{}/chromedriver_linux64.zip"
    latest_release_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    file_driver_zip = "./chromedriver_linux64.zip"
    file_driver = "./chromedriver"

    try:
        version = str(urlopen(latest_release_url).read().decode("utf-8"))
    except Exception as error_version:
        logging.error(error_version)
        version = '108.0.5359.71'

    urlretrieve(url.format(version), file_driver_zip)

    with ZipFile(file_driver_zip, 'r') as zip_ref:
        zip_ref.extractall()

    chmod(file_driver, 0o755)

    return file_driver


def get_chrome_browser(headless: bool = True):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}

    if headless:
        chrome_options.add_argument("--headless")

    try:
        return webdriver.Chrome(chrome_options=chrome_options)
    except WebDriverException:
        try:
            executable_path = ChromeDriverManager().install()
        except Exception:
            executable_path = run_binary_path_chrome()

        return webdriver.Chrome(
                executable_path=executable_path,
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
