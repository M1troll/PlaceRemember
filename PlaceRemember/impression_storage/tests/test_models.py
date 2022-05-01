from django.test import TestCase
from ..models import *


class ImpressionStorageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Run once to set up non-modified data for all class methods """
        User.objects.create(id=1, username='Пользователь', password='ЯПользователь228.',
                            first_name='Моё первое (шутка) имя', last_name='Моё второе (не шутка) имя',
                            email='IwantToBreakFree@mail.ru')

        Impression.objects.create(author_id=1, title='Место', description='Тут много написано',
                                  address='Moscow', location='55.7504461,37.6174943')

    def tearDown(self):
        """ Cleaning after each method """
        # Useless because of using TestCase
        pass

    def test_impression_title(self):
        impression = Impression.objects.get(pk=1)
        title_title = impression._meta.get_field('title').verbose_name

        self.assertEquals(title_title, 'Название места')

    def test_impression_description(self):
        impression = Impression.objects.get(pk=1)
        description_title = impression._meta.get_field('description').verbose_name

        self.assertEquals(description_title, 'Описание')

    def test_impression_address(self):
        impression = Impression.objects.get(pk=1)
        address_title = impression._meta.get_field('address').verbose_name

        self.assertEquals(address_title, 'Адрес')

    def test_impression_location(self):
        impression = Impression.objects.get(pk=1)
        location_title = impression._meta.get_field('location').verbose_name

        self.assertEquals(location_title, 'Координаты')

    def test_impression_author(self):
        impression = Impression.objects.get(pk=1)
        author_title = impression._meta.get_field('author').verbose_name

        self.assertEquals(author_title, 'Автор')

    def test_impression_str(self):
        impression = Impression.objects.get(pk=1)
        title = f'{impression}'

        self.assertEquals(title, impression.title)


class ProfileStorageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Run once to set up non-modified data for all class methods """
        User.objects.create(id=1, username='Пользователь', password='ЯПользователь228.',
                            first_name='Моё первое (шутка) имя', last_name='Моё второе (не шутка) имя',
                            email='IwantToBreakFree@mail.ru')

    def tearDown(self):
        """ Cleaning after each method """
        # Useless because of using TestCase
        pass

    def test_profile_created(self):
        try:
            profile = User.objects.get(pk=1).profile
        except Profile.DoesNotExist:
            profile = None

        self.assertFalse(profile is None)

    def test_profile_image_url(self):
        profile = User.objects.get(pk=1).profile
        image_url_title = profile._meta.get_field('image_url').verbose_name

        self.assertEquals(image_url_title, 'Фото')

    def test_profile_default_image_url(self):
        profile = User.objects.get(pk=1).profile
        url = profile.image_url

        self.assertEquals(url, '/static/images/base_avatar.png')

    def test_profile_str(self):
        user = User.objects.get(pk=1)
        profile = User.objects.get(pk=1).profile
        username = f'{profile}'

        self.assertEquals(username, user.username)
