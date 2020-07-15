from django import forms

from .models import Item, CV, Category

class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('name', 'addresses', 'mobile_number', 'email', 'personal_profile')

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('title',)
