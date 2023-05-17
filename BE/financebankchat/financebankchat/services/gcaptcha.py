import requests
from financebankchat.settings import RECAPTCHA_PRIVATE_KEY
"""
frontend check: https://developers.google.com/recaptcha/docs/v3
"""

def verify_recaptcha(g_token: str) -> bool:
    data = {
        'response': g_token,
        'secret': RECAPTCHA_PRIVATE_KEY,
    }
    resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result_json = resp.json()
    return result_json.get('success') is True