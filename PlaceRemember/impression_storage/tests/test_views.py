from django.test import Client, TestCase
from django.urls import reverse
from ..models import *
from social_django.models import UserSocialAuth


class ViewTemplateTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Run once to set up non-modified data for all class methods """
        pass

    def setUp(self):
        # Create an authorized client
        self.user = User.objects.create_user(username='Пользователь')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

        # Add impression in db for tests
        Impression.objects.create(author=self.user, title=f'Место', description=f'Тут много написано',
                                  address='Moscow', location='55.7504461,37.6174943')

    def test_pages_uses_correct_templates(self):
        # "name_html_template: reverse(name)"
        templates_pages_names = {
            'impression_storage/index.html': reverse('impression_storage:index'),
            'impression_storage/storage.html': reverse('impression_storage:storage'),
            'impression_storage/edit_storage.html': reverse('impression_storage:storage_edit', kwargs={'pk': 1}),
        }

        # Check that when accessing the name, the corresponding HTML template is called
        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template)


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Run once to set up non-modified data for all class methods """
        pass

    def setUp(self):
        # Create an authorized client
        self.user = User.objects.create_user(username='Пользователь')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_view(self):
        response = self.authorized_client.get(reverse('impression_storage:index'))
        self.assertEqual(response.status_code, 200)


class StorageViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Run once to set up non-modified data for all class methods """
        pass

    def setUp(self):
        # Create an authorized client
        self.user = User.objects.create_user(username='Пользователь1')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

        # Fill db with test records
        for i in range(20):
            Impression.objects.create(author=self.user, title=f'Место{i}', description=f'Тут много написано {i}',
                                      address='Moscow', location='55.7504461,37.6174943')

    def test_view_all_impressions(self):
        response = self.authorized_client.get(reverse('impression_storage:storage'))
        self.assertEqual(response.status_code, 200)

        for impression in response.context['impressions']:
            self.assertEqual(response.context['user'], impression.author)

        self.assertEqual(len(response.context['impressions']), 20)

    def test_new_impression(self):
        # Context
        kwargs = {
            "title": 'Важное место',
            "description": 'Тут реально много написано',
            "address": 'Moscow',
            "location": '55.7504461,37.6174943',
        }

        # Send context for new impression
        response = self.authorized_client.post(reverse('impression_storage:storage'), kwargs=kwargs)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/storage/')

        # Check impression created
        try:
            impression = Impression.objects.get(pk=20)
        except Impression.DoesNotExist:
            impression = None

        self.assertFalse(impression is None)


class EditStorageViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Run once to set up non-modified data for all class methods """
        pass

    def setUp(self):
        # Create an authorized client
        self.user = User.objects.create_user(username='Пользователь')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

        # Add impression in db for tests
        Impression.objects.create(author=self.user, title='Место', description='Тут много написано',
                                  address='Moscow', location='55.7504461,37.6174943')

    def test_view_get_is_fail(self):
        # Send context for not exist impression
        response = self.authorized_client.get(reverse('impression_storage:storage_edit', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'impression_storage/storage.html')

    def test_view_post_is_fail(self):
        # Send context for not exist impression
        response = self.authorized_client.get(reverse('impression_storage:storage_edit', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'impression_storage/storage.html')

    def test_view_post_is_correct(self):
        # Context
        cleaned_data = {
            'pk': 1,
            "title": 'Важное место',
            "description": 'Тут реально много написано',
            "address": 'Moscow',
            "location": '55.7504461,37.6174943',
        }

        # Send context for exist impression
        response = self.authorized_client.post(
            reverse('impression_storage:storage_edit', kwargs={'pk': 1}), cleaned_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/storage/')

        # Check the model changes
        impression = Impression.objects.get(pk=1)
        self.assertEqual(impression.title, cleaned_data['title'])
        self.assertEqual(impression.description, cleaned_data['description'])
        self.assertEqual(impression.address, cleaned_data['address'])
        self.assertEqual(impression.location, cleaned_data['location'])


class DeleteImpressionViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Run once to set up non-modified data for all class methods """
        pass

    def setUp(self):
        # Create an authorized client
        self.user = User.objects.create_user(username='Пользователь')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

        # Add impression in db for tests
        Impression.objects.create(author=self.user, title='Место', description='Тут много написано',
                                  address='Moscow', location='55.7504461,37.6174943')

    def test_delete_impression_is_correct(self):
        # Send context for exist impression
        response = self.authorized_client.get(reverse('impression_storage:delete_impression', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/storage/')

        # Check impression deleted
        impression = Impression.objects.get(pk=1)
        self.assertTrue(impression.is_deleted)

        # Check the editing of the deleted model
        response = self.authorized_client.get(reverse('impression_storage:storage_edit', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/storage/')

