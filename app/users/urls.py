from django.urls import path
from users.views import registration, profile, logout, users_cart, UserLoginView


app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", registration, name="registration"),
    path("profile/", profile, name="profile"),
    path("users_cart/", users_cart, name="users_cart"),
    path("logout/", logout, name="logout"),
]
