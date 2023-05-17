from django.urls import path
from api.authentication.views import register_user_view

urlpatterns = [
    path('register/', register_user_view.as_view()),
]
