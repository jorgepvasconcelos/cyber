from task_app.utils.captcha import get_recaptcha_token
from task_app.utils.selenium import get_chrome_selenium_tool_kit
from task_app.celery_app import app


@app.task(name='send_form_cyber')
def send_form_cyber():
    selenium_kit = get_chrome_selenium_tool_kit()
    try:
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
        if not recaptcha_token:
            raise ValueError("Didn't receive recaptcha token")

        script = f'document.getElementById("g-recaptcha-response").innerHTML="{recaptcha_token}";'
        selenium_kit.driver.execute_script(script)

        qs_submit_bottom = '[type="submit"]'
        selenium_kit.click(query_selector=qs_submit_bottom)

    except Exception as e:
        selenium_kit.driver.quit()
        raise e

    selenium_kit.driver.quit()
    return "[Task] Success"
