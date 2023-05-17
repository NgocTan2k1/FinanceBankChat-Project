from django.urls import path
from api.cryption.views import get_token_view

urlpatterns = [
    path('',get_token_view.as_view()),
]
