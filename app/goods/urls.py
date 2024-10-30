from django.urls import path
from goods.views import catalog, product


app_name = "goods"

urlpatterns = [
    path("<slug:category_slug>/", catalog, name="catalog"),
    path("<slug:category_slug>/<int:page>/", catalog, name="catalog"),
    path("product/<slug:product_slug>/", product, name="product"),
]
