from django import forms
from django.db import models

from api.models import Client



class ClientModifyForm(forms.Form):
    id = forms.CharField(label='', widget='', required=False)
    addr = forms.CharField(required=False)
    user = forms.CharField(required=False)
    application = forms.CharField(required=False)
    remark = forms.CharField(required=False)


    def clean_id(self):
        id = self.cleaned_data.get('id', 0)
        if not id.isdigit():
            raise forms.ValidationError('操作对象不存在')
        try:
            Client.objects.get(id=id)
        except models.ObjectDoesNotExist as e:
            raise forms.ValidationError('操作对象不存在')
        return id

    def clean_addr(self):
        addr = self.cleaned_data.get('addr', '')
        if len(addr) > 256:
            raise forms.ValidationError('地址不能超过256个字符')
        return addr

    def clean_user(self):
        user = self.cleaned_data.get('user', '')
        if len(user) > 64:
            raise forms.ValidationError('用户名不能超过64个字符')
        return user

    def clean_application(self):
        application = self.cleaned_data.get('application', '')
        if len(application) > 64:
            raise forms.ValidationError('应用不能超过64个字符')
        return application


    def clean_remark(self):
        remark = self.cleaned_data.get('remark', '')
        if len(remark) > 256:
            raise forms.ValidationError('备注不能超过256个字符')
        return remark