from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


# Вариант 1. Максимально отделяем бекенд от фронтенда
class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "password"]


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


# Вариант 2. Стандартный вариант
# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(
#         label="Имя пользователя!!!",
#         widget=forms.TextInput(
#             attrs={
#                 "autofocus": True,
#                 "class": "form-control",
#                 "id": "username",
#                 "placeholder": "Введите ваше имя пользователя",
#             }
#         ),
#     )

#     password = forms.CharField(
#         label="Пароль",
#         widget=forms.PasswordInput(
#             attrs={
#                 "autocomplete": "current-password",
#                 "class": "form-control",
#                 "id": "password",
#                 "placeholder": "Введите ваш пароль",
#             }
#         ),
#     )

#     class Meta:
#         model = User
#         fields = ["username", "password"]
