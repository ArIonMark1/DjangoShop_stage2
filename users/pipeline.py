# from collections import OrderedDict
# from datetime import datetime
# from urllib.parse import urlencode, urlunparse
#
# import requests
# from django.utils import timezone
# from social_core.exceptions import AuthForbidden
#
# from users.models import ProfileUser
#
#
# def save_user_profile(backend, user, response, *args, **kwargs):
#     if backend.name != 'google-oauth2':
#         return
#     api_url = urlunparse(('https',
#                           'googleapis.com',
#                           '/method/users.get',
#                           None,
#                           urlencode(OrderedDict(fields=','.join(('image', 'sex', 'about')),
#                                                 access_token=response['access_token'],
#                                                 v='1')),
#                           None
#                           ))
#
#     resp = requests.get(api_url)
#     if resp.status_code != 200:
#         print(resp.json())
#         return
#
#     data = resp.json()['response'][0]
#     if data['sex']:
#         user.shopuserprofile.gender = ProfileUser.MALE if data['sex'] == 2 else ProfileUser.FEMALE
#
#     if data['about']:
#         user.shopuserprofile.aboutMe = data['about']
#
#     if data['image']:
#         user.image = data['image']
#
#     # if data['bdate']:
#     #     bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
#     #
#     #     age = timezone.now().date().year - bdate.year
#     #     if age < 18:
#     #         user.delete()
#     #         raise AuthForbidden('social_core.backends.vk.VKOAuth2')
#
#     user.save()
