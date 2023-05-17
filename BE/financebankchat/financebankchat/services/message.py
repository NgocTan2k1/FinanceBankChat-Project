import datetime
import pytz
import base64
from financebankchat.helper.npl_helper import add_noise_to_money
from financebankchat.services.cryption import decrypt_message, encrypt_message
from core.models import cryption


def questions_gpt(message , key_pair):
    now = datetime.datetime.now()
    if now > key_pair.live_time:
        return False, "token expired",
    crawl_text = decrypt_message(base64.b64decode(message), key_pair.pri_key)
    return True, crawl_text


def encrypt_ques(raw_text, public_key):
    return encrypt_message(raw_text.encode(), public_key)


def encrypt_question(question_raw, user):
    try:
        return (
            questions_gpt(question_raw, key_pair)
            if (key_pair := cryption.objects.filter(user=user).first())
            else (False, 'Token not found')
        )
    except Exception as e:
        return False, "lỗi câu hỏi không hợp lệ"

