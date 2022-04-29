from django import forms
from location_field.forms.plain import PlainLocationField

from .models import Impression


class ImpressionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "field char"}), label='Название')
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "field textarea"}), label='Описание')

    address = forms.CharField(widget=forms.TextInput(attrs={"class": "field"}), label='Адрес', max_length=200,
                              required=False)
    location = PlainLocationField(based_fields=['address'], initial='56.00637898153531,92.86683082580566', label='Координаты')

    class Meta:
        model = Impression
        fields = ['title', 'description', 'address', 'location']
