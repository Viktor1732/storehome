from django.shortcuts import render


def login(request):
    context = {
        "title": "StoreHome - Login",
    }
    return render(request, "users/login.html", context=context)


def registration(request):
    context = {
        "title": "StoreHome - Registration",
    }
    return render(request, "users/registration.html", context=context)


def profile(request):
    context = {
        "title": "StoreHome - Profile",
    }
    return render(request, "users/profile.html", context=context)


def logout(request):
    pass
