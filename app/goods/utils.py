"""
Объяснение кода:
vector = SearchVector('name', 'description'):

Создает объект SearchVector, который объединяет поля name и description. 
Это позволяет выполнять полнотекстовый поиск по обоим полям одновременно.
query = SearchQuery(query):

Создает объект SearchQuery, который представляет собой сам текст запроса, 
который будет использоваться для поиска. Это позволяет Django интерпретировать 
строку запроса как поисковый запрос.
Products.objects.annotate(rank=SearchRank(vector, query)):

Использует метод annotate для добавления нового поля rank к каждому объекту в QuerySet.
SearchRank(vector, query) вычисляет оценку соответствия (ранг) для каждого 
объекта на основе того, насколько хорошо они соответствуют запросу. Чем выше значение rank, 
тем более релевантен объект запросу.
.order_by("-rank"):

Сортирует результаты по убыванию rank, то есть сначала будут показаны наиболее 
релевантные результаты. Знак минус перед rank указывает на сортировку по убыванию.
Итог:
Этот код эффективно улучшает поиск, возвращая объекты Products, которые не только 
соответствуют запросу, но и упорядочены по релевантности. Это делает поиск более удобным 
для пользователя, так как наиболее подходящие результаты будут показаны первыми. Такой подход, 
с использованием SearchVector, SearchQuery и SearchRank, является стандартным для реализации 
мощного полнотекстового поиска в Django.
"""

from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

# from django.db.models import Q

from goods.views import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel="<span style='background-color: yellow;'>",
            stop_sel="</span>",
        )
    )

    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel="<span style='background-color: yellow;'>",
            stop_sel="</span>",
        )
    )

    return result

    # annotate — метод, который добавляет вычисляемое поле search к каждому объекту в QuerySet.
    # SearchVector — класс, который создаёт вектор для полнотекстового поиска, объединяя поля name и description товаров.
    # filter(search=query): После аннотации, этот вызов фильтрует объекты Products, чтобы вернуть только те, у которых поле search соответствует query.

    # return Products.objects.annotate(search=SearchVector("name", "description")).filter(search=query)

    # keywords = [word for word in query.split() if len(word) > 2]
    # q_object = Q()

    # for token in keywords:
    #     q_object |= Q(name__icontains=token)
    #     q_object |= Q(description__icontains=token)

    # return Products.objects.filter(q_object)
