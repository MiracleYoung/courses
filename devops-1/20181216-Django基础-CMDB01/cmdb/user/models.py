from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import hashlib, os, base64


class User(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128, default='')
    age = models.IntegerField()
    telephone = models.CharField(max_length=32)
    email = models.EmailField()
    register_time = models.DateTimeField(auto_now_add=True)
    login_time = models.DateTimeField()
    qwe = models.CharField(max_length=12, default='qwe')


    def check_password(self, password):
        _salt, _hash = self.password.split('$')
        _md5 = hashlib.md5()
        _md5.update(_salt.encode() + password.encode())
        return _hash == _md5.hexdigest()


    @classmethod
    def login(cls, name, password):
        try:
            user = cls.objects.get(name=name)
            if user.check_password(password):
                user.login_time = timezone.now()
                user.save()
                return user
        except ObjectDoesNotExist:
            print(f'login error, name: {name}, password: {password}')
        return

    def set_password(self, password: str):
        _salt = base64.b64encode(os.urandom(8))
        _md5 = hashlib.md5()
        _md5.update(_salt + password.encode())
        self.password = f'{_salt.decode()}${_md5.hexdigest()}'


    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'telephone': self.telephone,
            'email': self.email,
        }




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