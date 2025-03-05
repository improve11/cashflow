import django_filters
from .models import Transaction

class TransactionFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(
        field_name='date',
        label='Дата (период)',
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'})
    )
    
    class Meta:
        model = Transaction
        fields = {
            'status': ['exact'],
            'type': ['exact'],
            'category': ['exact'],
            'subcategory': ['exact'],
        }