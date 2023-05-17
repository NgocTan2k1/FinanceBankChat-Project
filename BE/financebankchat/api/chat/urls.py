from django.urls import path
from api.chat.views import chat_views

urlpatterns = [
    path('', chat_views.as_view()),
]
