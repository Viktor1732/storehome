from carts.models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        # Используем select_related для оптимизации запроса и получения данных о продукте (из таблицы Product)
        return Cart.objects.filter(user=request.user).select_related("product")

    if not request.session.session_key:
        request.session.create()

    # Опять же используем select_related для оптимизации запроса, чтобы сразу подгрузить связанные продукты
    return Cart.objects.filter(session_key=request.session.session_key).select_related("product")
