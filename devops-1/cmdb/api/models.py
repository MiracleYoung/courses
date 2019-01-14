from django.db import models

from django.utils import timezone

import datetime

# Create your models here.


class Attr2DictMixin:
    def as_dict(self):
        _dict = {}
        for _key, _value in self.__dict__.items():
            if isinstance(_value, (int, float, str, bool)):
                _dict[_key] = _value
            elif isinstance(_value, (datetime.datetime)):
                _dict[_key] = str(_value)
        return _dict

class Client(Attr2DictMixin, models.Model):
    uuid = models.CharField(max_length=64, unique=True, default='')
    hostname = models.CharField(max_length=128, default='')
    ip = models.GenericIPAddressField(default='0.0.0.0')
    mac = models.CharField(max_length=32)
    platform = models.CharField(max_length=128, default='CentOS')
    arch = models.CharField(max_length=16, default='')
    cpu = models.IntegerField(default=0)
    mem = models.BigIntegerField(default=0)
    pid = models.IntegerField(default=0)
    time = models.FloatField(default=0)

    user = models.CharField(max_length=64, default='')
    application = models.CharField(max_length=64, default='')
    addr = models.CharField(max_length=256, default='')
    remark = models.CharField(max_length=256, default='')

    heartbeat_time = models.DateTimeField(auto_now_add=True)
    register_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    @property
    def is_online(self):
        return timezone.now() - self.heartbeat_time < datetime.timedelta(minutes=5)


    @classmethod
    def register(cls, uuid, **kwargs):
        '''
        除了注册外，还具有上报信息的作用
        '''
        _instance = None
        _created = False
        # 判断是否重复注册
        try:
            _instance = cls.objects.get(uuid=uuid)
        except models.ObjectDoesNotExist:
            _instance = cls()
            _created = True
            setattr(_instance, 'uuid', uuid)

        for _key, _value in kwargs.items():
            if hasattr(_instance, _key):
                setattr(_instance, _key, _value)

        _instance.save()
        return _created, _instance

    @classmethod
    def heartbeat(cls, uuid):
        try:
            _instance = cls.objects.get(uuid=uuid)
            _instance.heartbeat_time = timezone.now()
            _instance.save()
            return True
        except models.ObjectDoesNotExist:
            return False


    def as_dict(self):
        _dict = super().as_dict()
        _dict['is_online'] = self.is_online
        return _dict


    def __str__(self):
        return f'<Client: {self.uuid}>'





class Resource(Attr2DictMixin, models.Model):
    '''
    监控
    '''
    uuid = models.CharField(max_length=64, unique=True, default='')
    time = models.DateTimeField(auto_now_add=True)
    cpu = models.FloatField(default=0)
    mem = models.FloatField(default=0)

    @classmethod
    def create(cls, uuid, **kwargs):
        _instance = cls()
        _instance.uuid = uuid
        # setattr(_instance, 'uuid', uuid)
        for _key, _value in kwargs.items():
            if hasattr(_instance, _key):
                setattr(_instance, _key, _value)

        _instance.save()
        return _instance


# /clients/uuid/
# body = {uuid: , hostname: , ip: , cpu: } => **kwargs
# {a: , b: , c: }