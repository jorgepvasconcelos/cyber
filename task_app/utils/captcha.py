from twocaptcha import TwoCaptcha

from settings import CAPTCHA_API_KEY


def get_recaptcha_token(site_key: str, site_url: str) -> str | None:
    solver = TwoCaptcha(CAPTCHA_API_KEY)

    try:
        result = solver.recaptcha(sitekey=site_key, url=site_url)

    except Exception as e:
        print(e)
        return None

    else:
        return result["code"]
