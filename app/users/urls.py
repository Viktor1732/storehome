from django.urls import path
from users.views import profile, logout, users_cart, UserLoginView, UserRegistrationView


app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("profile/", profile, name="profile"),
    path("users_cart/", users_cart, name="users_cart"),
    path("logout/", logout, name="logout"),
]
