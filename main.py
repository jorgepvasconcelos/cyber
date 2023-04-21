from selenium.webdriver import Chrome
from selenium_toolkit import SeleniumToolKit

driver = Chrome(executable_path='./chromedriver')
selenium_kit = SeleniumToolKit(driver=driver)

selenium_kit.goto(url="https://cyberintelligencehouse.com/services-page/")

qs_name = '[name="name_user"]'
selenium_kit.fill(text='',query_selector=qs_name)

qs_company_name = '[name="company_name"]'
selenium_kit.fill(text='',query_selector=qs_company_name)

qs_email = '[name="email"]'
selenium_kit.fill(text='',query_selector=qs_email)

qs_phone = '[name="phone"]'
selenium_kit.fill(text='',query_selector=qs_phone)

selenium_kit.find_element_by_text(text="I agree with the Legal Terms and Data Protection Policy").click()

# Captcha