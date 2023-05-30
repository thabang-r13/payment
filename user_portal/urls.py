from django.urls import path
from . import views

urlpatterns = [
    path('user_portal/', views.user_portal, name='user_portal'),
]
