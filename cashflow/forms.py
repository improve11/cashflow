from django import forms
from .models import *

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.type.category_set

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set
            
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        type = cleaned_data.get('type')
        
        if category and category.type != type:
            raise forms.ValidationError("Выбранная категория не принадлежит выбранному типу!")
        
        subcategory = cleaned_data.get('subcategory')
        if subcategory and subcategory.category != category:
            raise forms.ValidationError("Выбранная подкатегория не принадлежит выбранной категории!")
        
        if cleaned_data.get('amount') <= 0:
            raise forms.ValidationError("Сумма должна быть положительной!")
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']