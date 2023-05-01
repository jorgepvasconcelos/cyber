from selenium_toolkit import SeleniumToolKit
from selenium import webdriver

from settings import HOST_SELENIUM_GRID


def get_chrome_selenium_tool_kit() -> SeleniumToolKit:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(command_executor=f'http://{HOST_SELENIUM_GRID}:4444/wd/hub', options=options)
    selenium_kit = SeleniumToolKit(driver=driver)

    return selenium_kit
