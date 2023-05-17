from financebankchat.helper.application_helper import validate_email
from django.contrib.auth.models import User


def register_user(username: str, password1: str, password2: str, email: str):
    if not validate_email(email):
        return False, 'Email không hợp lệ'
    
    if password1 != password2:
        return False, 'Hai mật khẩu không trùng nhau'
    
    if User.objects.filter(username=username).exists():
        return False, 'User đã tồn tại'
    
    User.objects.create_user(
        username=username,
        email=email,
        password=password1
    )
    return True, "Đăng ký thành công"