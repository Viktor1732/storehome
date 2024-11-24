from django.urls import path
from users.views import logout, UserCartView, UserLoginView, UserRegistrationView, UserProfileView


app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("users_cart/", UserCartView.as_view() , name="users_cart"),
    path("logout/", logout, name="logout"),
]
