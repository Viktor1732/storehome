from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from orders.models import Order, OrderItem
from carts.models import Cart
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"Вы вошли в профиль как {username}!")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                # Если параметр "next" существует и не равен маршруту выхода (logout), перенаправляем на указанную страницу
                redirect_page = request.POST.get("next", None)
                if redirect_page and redirect_page != reverse("user:logout"):
                    return HttpResponseRedirect(request.POST.get("next"))

                # Если параметра "next" нет, перенаправляем на главную страницу
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "StoreHome - Login",
        "form": form,
    }
    return render(request, "users/login.html", context=context)


def registration(request):
    if request.POST:
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(
                request,
                f"Вы успешно зарегистрировались и вошли в профиль как {user.username}!",
            )
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {
        "title": "StoreHome - Registration",
        "form": form,
    }
    return render(request, "users/registration.html", context=context)


@login_required  # ограничение доступа для неаутентифицированных пользователей
def profile(request):
    if request.POST:
        form = UserProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = UserProfileForm(instance=request.user)

    orders = (
        Order.objects.filter(user=request.user).prefetch_related(
            Prefetch(
                "orderitem_set",
                queryset=OrderItem.objects.select_related("product"),
            )
        ).order_by("-id")
    )

    context = {
        "title": "StoreHome - Profile",
        "form": form,
        "orders": orders,
    }
    return render(request, "users/profile.html", context=context)


def users_cart(request):
    return render(request, "users/users_cart.html")


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, f"Вы вышли из профиля!")
    return redirect(reverse("main:index"))
