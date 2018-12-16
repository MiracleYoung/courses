from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128, default='')
    age = models.IntegerField()
    telephone = models.CharField(max_length=32)
    email = models.EmailField()
    register_time = models.DateTimeField(auto_now_add=True)
    login_time = models.DateTimeField()
    qwe = models.CharField(max_length=12, default='qwe')

    @classmethod
    def login(cls, name, password):
        try:
            user = cls.objects.get(name=name, password=password)
            user.login_time = timezone.now()
            user.save()
        except ObjectDoesNotExist:
            print(f'login error, name: {name}, password: {password}')
        return user



'''
BEGIN;
--
-- Create model User
--
CREATE TABLE `user_user` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    `name` varchar(128) NOT NULL, 
    `age` integer NOT NULL, 
    `telephone` varchar(32) NOT NULL, 
    `email` varchar(254) NOT NULL, 
    `register_time` datetime(6) NOT NULL, 
    `login_time` datetime(6) NOT NULL);
COMMIT;
'''