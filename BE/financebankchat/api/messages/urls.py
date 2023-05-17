from django.urls import path
from api.messages.views import post_message_view

urlpatterns = [
    path('',post_message_view.as_view()),
]
