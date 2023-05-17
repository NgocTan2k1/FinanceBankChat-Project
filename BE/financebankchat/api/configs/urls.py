from django.urls import path
from api.configs.views import config_views, stock_views, provider_views

urlpatterns = [
    path('provider/', provider_views.as_view()),
    path('stock/', stock_views.as_view()),
    path('login/', config_views.as_view()),
]
