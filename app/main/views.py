from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "StoreHome - Главная"
        context["content"] = "Магазин мебелеи StoreHome"  
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "StoreHome - О Нас!"
        context["content"] = "StoreHome - Магазин для Всех!"
        context["text_on_page"] = "Наш магазин действительно хорош! Мы крутые ребята!"
        return context
