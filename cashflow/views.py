from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
import csv
from .models import *
from .forms import *
from .filtres import TransactionFilter

class TransactionListView(ListView):
    model = Transaction
    template_name = 'cashflow/index.html'
    context_object_name = 'transactions'
    paginate_by = 25
    
    def get_queryset(self):
        return TransactionFilter(self.request.GET, queryset=super().get_queryset()).qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TransactionFilter(self.request.GET, queryset=self.get_queryset())
        return context

# CRUD для транзакций
class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'cashflow/transaction_form.html'
    success_url = reverse_lazy('index')

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'cashflow/transaction_form.html'
    success_url = reverse_lazy('index')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'cashflow/transaction_confirm_delete.html'
    success_url = reverse_lazy('index')

# CRUD для справочников
class DictionaryManageView(ListView):
    template_name = 'cashflow/manage_dictionaries.html'
    context_object_name = 'dictionaries'
    
    def get_queryset(self):
        return {
            'statuses': Status.objects.all(),
            'types': Type.objects.all(),
            'categories': Category.objects.all(),
            'subcategories': Subcategory.objects.all(),
        }

class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'cashflow/generic_form.html'
    success_url = reverse_lazy('manage')

class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'cashflow/generic_form.html'
    success_url = reverse_lazy('manage')

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'cashflow/generic_confirm_delete.html'
    success_url = reverse_lazy('manage')

# Аналогичные классы для Type, Category, Subcategory
class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'cashflow/generic_form.html'
    success_url = reverse_lazy('manage')

class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'cashflow/generic_form.html'
    success_url = reverse_lazy('manage')

class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'cashflow/generic_confirm_delete.html'
    success_url = reverse_lazy('manage')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'cashflow/generic_form.html'
    success_url = reverse_lazy('manage')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'cashflow/generic_form.html'
    success_url = reverse_lazy('manage')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'cashflow/generic_confirm_delete.html'
    success_url = reverse_lazy('manage')

class SubcategoryCreateView(CreateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'cashflow/generic_form.html'
    success_url = reverse_lazy('manage')

class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'cashflow/generic_form.html'
    success_url = reverse_lazy('manage')

class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    template_name = 'cashflow/generic_confirm_delete.html'
    success_url = reverse_lazy('manage')

# AJAX представления
def load_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id)
    return render(request, 'cashflow/category_dropdown_list_options.html', {'categories': categories})

def load_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id)
    return render(request, 'cashflow/subcategory_dropdown_list_options.html', {'subcategories': subcategories})

# Экспорт данных
def export_transactions(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Дата', 'Статус', 'Тип', 'Категория', 'Подкатегория', 'Сумма', 'Комментарий'])
    
    transactions = TransactionFilter(request.GET, Transaction.objects.all()).qs
    for t in transactions:
        writer.writerow([
            t.date.strftime("%d.%m.%Y %H:%M"),
            t.status.name,
            t.type.name,
            t.category.name,
            t.subcategory.name,
            t.amount,
            t.comment
        ])
    
    return response