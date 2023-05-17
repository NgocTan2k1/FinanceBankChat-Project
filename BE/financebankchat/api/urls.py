from django.urls import path, include

urlpatterns = [
    path('v1/bank/', include('api.bank.urls')),
    path('v1/cryption', include('api.cryption.urls')),
    path('v1/messages', include('api.messages.urls')),
    path('v1/authentication/', include('api.authentication.urls')),
    path('v1/chat/', include('api.chat.urls')),
    path('v1/configs/', include('api.configs.urls')),
]
