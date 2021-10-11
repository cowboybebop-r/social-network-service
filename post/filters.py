from post.models import PostRate

from django_filters import rest_framework as filters


class DateRangeFilterSet(filters.FilterSet):
    date_from = filters.DateFilter(field_name='create_at', lookup_expr='gte')
    date_to = filters.DateFilter(field_name='create_at', lookup_expr='lte')

    class Meta:
        model = PostRate
        fields = ('date_from', 'date_to')
