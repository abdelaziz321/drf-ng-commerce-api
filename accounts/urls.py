from django.urls import path
from .views.authentication import register_view, login_view, me_view

urlpatterns = [
    # auth
    path('auth/register', register_view),
    path('auth/login', login_view),
    path('auth/me', me_view),
]
