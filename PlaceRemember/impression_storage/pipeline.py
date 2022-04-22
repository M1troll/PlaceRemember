from django.contrib.auth.models import User


def get_avatar(backend, response, user=None, *args, **kwargs):

    if user is None:
        return

    if backend.name == 'vk-oauth2':
        url = response.get('user_photo', '')
    else:
        url = None

    if url:
        user.profile.image_url = url
        user.profile.save()
