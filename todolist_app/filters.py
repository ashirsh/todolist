from django_filters import rest_framework as drf_filter

from .models import ToDoList


class ToDoListFilter(drf_filter.FilterSet):
    importance_filter = drf_filter.BooleanFilter(
        field_name='important',
        help_text='Значимость'
    )

    public_filter = drf_filter.BooleanFilter(
        field_name='public',
        help_text='Публичность'
    )

    instance_filter = drf_filter.CharFilter(
        field_name='status',
        help_text='Состояние'
    )

    min_view = drf_filter.NumberFilter('views', lookup_expr='gte')
    max_view = drf_filter.NumberFilter('views', lookup_expr='lte')
    author = drf_filter.NumberFilter('author__pk')

    class Meta:
        model = ToDoList
        fields = (
            'important',
            'public',
            'status',
            'author',
        )
