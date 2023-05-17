from django.http import Http404
import re
import random

def number_type(number):
    if number.isdigit():
        return int(number)
    elif number.replace(".","").isdigit():
        return float(number)
    else:
        return(type(number))

def add_noise_to_money(sentence):
    pattern_unit = r'(\d+)\s*? (tỷ|triệu|nghìn|đồng|đ|d|vnđ|VNĐ|VND|vnd)'
    rs = re.sub(pattern_unit, convert_to_unit, sentence)

    pattern_noice = r"(\d+)\s*? (triệu VNĐ)"
    rs = re.sub(pattern_noice, replace_money, rs)
    return rs

def replace_money(match, prob=0.9, min_noise=0.1, max_noise=0.3):
    money_str = match.group(1)
    money_form = money_str.split()
    money = number_type(money_form[0].replace(",", ""))
    if random.random() >= prob:
        return money_str
    noise = random.uniform(min_noise, max_noise) * money
    sign = random.choice([-1, 1])
    noisy_money = money + sign * noise
    return "{:.0f}".format(noisy_money) + " đơn vị tiền"

def convert_to_unit(mat):
    unit = mat.group(1)
    zeros = {
        "tỷ": "0"*9,
        "triệu": "0"*6,
        "nghìn": "0"*3,
        "đồng" : "",
        "đ": "",
        "d": "",
        "vnd": "",
        "VND":"",
        "vnđ":"",
        "VNĐ":""
    }
    unit += zeros[mat.group(2)]
    unit = number_type(unit)
    return "{:.0f}".format(unit/1000000.0) + " triệu VNĐ"