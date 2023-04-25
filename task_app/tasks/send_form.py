from selenium import webdriver
from selenium_toolkit import SeleniumToolKit

from task_app.captcha import get_recaptcha_token
from task_app.celery_app import app
from settings import HOST_SELENIUM_GRID


@app.task(name='send_form_cyber')
def send_form_cyber():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(command_executor=f'http://{HOST_SELENIUM_GRID}:4444/wd/hub', options=options)
    selenium_kit = SeleniumToolKit(driver=driver)

    site_url = "https://cyberintelligencehouse.com/services-page/"
    selenium_kit.goto(url=site_url)

    qs_name = '[name="name_user"]'
    selenium_kit.fill(text='fake name', query_selector=qs_name)

    qs_company_name = '[name="company_name"]'
    selenium_kit.fill(text='fake company', query_selector=qs_company_name)

    qs_email = '[name="email"]'
    selenium_kit.fill(text='fake5656_email@empresa.net.com', query_selector=qs_email)

    qs_phone = '[name="phone"]'
    selenium_kit.fill(text='1145658978', query_selector=qs_phone)

    selenium_kit.find_element_by_text(text="I agree with the Legal Terms and Data Protection Policy").click()

    qs_data_sitekey = "span[data-sitekey]"
    site_key = selenium_kit.get_attribute(query_selector=qs_data_sitekey, attribute="data-sitekey")

    recaptcha_token = get_recaptcha_token(site_key=site_key, site_url=site_url)
    script = f'document.getElementById("g-recaptcha-response").innerHTML="{recaptcha_token}";'
    driver.execute_script(script)

    qs_submit_bottom = '[type="submit"]'
    selenium_kit.click(query_selector=qs_submit_bottom)
    selenium_kit.driver.quit()

    return 'this is a success task'
