from django.urls import path
from . import views

urlpatterns = [
    # Transactions
    path('', views.TransactionListView.as_view(), name='index'),
    path('create/', views.TransactionCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.TransactionUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='delete'),
    
    # Dictionaries
    path('manage/', views.DictionaryManageView.as_view(), name='manage'),
    
    # Status
    path('status/add/', views.StatusCreateView.as_view(), name='status_create'),
    path('status/<int:pk>/edit/', views.StatusUpdateView.as_view(), name='status_edit'),
    path('status/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),
    
    # Type
    path('type/add/', views.TypeCreateView.as_view(), name='type_create'),
    path('type/<int:pk>/edit/', views.TypeUpdateView.as_view(), name='type_edit'),
    path('type/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='type_delete'),
    
    # Category
    path('category/add/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    
    # Subcategory
    path('subcategory/add/', views.SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory/<int:pk>/edit/', views.SubcategoryUpdateView.as_view(), name='subcategory_edit'),
    path('subcategory/<int:pk>/delete/', views.SubcategoryDeleteView.as_view(), name='subcategory_delete'),
    
    # AJAX
    path('load-categories/', views.load_categories, name='load_categories'),
    path('load-subcategories/', views.load_subcategories, name='load_subcategories'),
    
    # Export
    path('export/', views.export_transactions, name='export'),
]