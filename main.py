from selenium import webdriver
from selenium_toolkit import SeleniumToolKit

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
selenium_kit = SeleniumToolKit(driver=driver)

selenium_kit.goto(url="https://cyberintelligencehouse.com/services-page/")

qs_name = '[name="name_user"]'
selenium_kit.fill(text='fake name',query_selector=qs_name)

qs_company_name = '[name="company_name"]'
selenium_kit.fill(text='fake company',query_selector=qs_company_name)

qs_email = '[name="email"]'
selenium_kit.fill(text='fake5656_email@hotmail.com',query_selector=qs_email)

qs_phone = '[name="phone"]'
selenium_kit.fill(text='1145658978',query_selector=qs_phone)

selenium_kit.find_element_by_text(text="I agree with the Legal Terms and Data Protection Policy").click()

selenium_kit.driver.quit()

# Captcha