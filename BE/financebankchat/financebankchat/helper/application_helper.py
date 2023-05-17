import json
import re

def str_to_bool(s: str or bool) -> bool:
    if type(s) == bool:
        return s
    from distutils.util import strtobool
    return bool(strtobool(s))


def validate_email(email: str) -> bool:
    pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def load_json(text):
    try:
        return json.loads(text)
    except Exception:
        return ""



    