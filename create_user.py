# coding:utf-8
"""
直接在DjangoUser中创建一个新的用户
"""

import os
import django
import getpass

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gg_server.settings")
django.setup()


if __name__ == '__main__':
    from django.contrib.auth.models import User

    while True:
        username = input('Username: ')
        if User.objects.filter(username=username).exists():
            print('\033[0;33m{}\033[0m'.format('用户名重复'))
        else:
            break
    password = getpass.getpass()
    user = User.objects.create(username=username)
    user.set_password(raw_password=password)
    user.save()
print('\033[0;32m{}\033[0m'.format('SUCCESS'))
