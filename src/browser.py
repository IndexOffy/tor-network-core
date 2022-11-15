from os import system
from urllib.request import urlretrieve

from selenium import webdriver
from tbselenium.tbdriver import TorBrowserDriver
from webdriver_manager.chrome import ChromeDriverManager

from src.settings import url_tor_browser, file_tor_browser


class Browser():

    def __init__(self, driver: str, headless: bool = True) -> None:
        self.headless = headless
        self.driver = getattr(self, f'get_{driver}_browser')()

    def get_chrome_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        if self.headless:
            chrome_options.add_argument("--headless")
        
        executable_path = ChromeDriverManager().install()
        return webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

    def get_tor_browser(self):
        option = webdriver.FirefoxOptions()
        option.headless = self.headless

        urlretrieve(url_tor_browser, file_tor_browser)
        system(f'tar -xvJf {file_tor_browser}')
        system('sudo apt-get install tor')

        return TorBrowserDriver('./tor-browser_en-US', options=option)
