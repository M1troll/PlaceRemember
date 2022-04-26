from django import forms

from .models import Impression


class ImpressionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "field"}), label='Название')
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "field"}), label='Описание')

    lon = forms.FloatField(widget=forms.NumberInput(attrs={"class": "field"}), label='Долгота')
    lat = forms.FloatField(widget=forms.NumberInput(attrs={"class": "field"}), label='Широта')

    class Meta:
        model = Impression
        fields = ['title', 'description', 'lon', 'lat']
