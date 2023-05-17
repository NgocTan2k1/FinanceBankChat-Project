from django.urls import path, include
from django.core.exceptions import PermissionDenied, ViewDoesNotExist, RequestAborted, SuspiciousOperation
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.views import login_gcaptcha, processdata
from financebankchat.helper.npl_helper import add_noise_to_money


def trigger_error(request):  # NOSONAR
    division_by_zero = 1 / 0  # NOSONAR
    print(division_by_zero)
    raise SuspiciousOperation


def permission_denied_view(request):
    raise PermissionDenied


def resource_not_exist(request):
    raise ViewDoesNotExist


def request_aborted(request):
    raise RequestAborted

urlpatterns = [
    # ERROR HANDLING
    path('403/', permission_denied_view),
    path('404/', resource_not_exist),
    path('400/', request_aborted),
    path('500/', request_aborted),

    # API
    path('token/', login_gcaptcha.as_view(), name='login_api'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_api'),
    # path('drf/', include('rest_framework.urls')),  # DRF Login
    path('api/', include('api.urls')),
    path('run_data/', processdata.as_view()),
]

# add_noise_to_money("Tôi có 5 tỷ")