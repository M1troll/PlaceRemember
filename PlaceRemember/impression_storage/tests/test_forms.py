from django.test import TestCase
from ..forms import *


class ImpressionFormTest(TestCase):

    def test_title_field(self):
        form = ImpressionForm()
        label = form.fields['title'].label

        self.assertTrue(label == 'Название')

    def test_description_field(self):
        form = ImpressionForm()
        description = form.fields['description'].label

        self.assertTrue(description == 'Описание')

    def test_address_field(self):
        form = ImpressionForm()
        address = form.fields['address'].label

        self.assertTrue(address == 'Адрес')

    def test_location_field(self):
        form = ImpressionForm()
        location = form.fields['location'].label

        self.assertTrue(location == 'Координаты')
