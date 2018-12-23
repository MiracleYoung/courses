from django import forms

from user.models import User

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, label='旧密码')
    password = forms.CharField(widget=forms.PasswordInput, label='新密码')
    password2 = forms.CharField(widget=forms.PasswordInput, label='再次输入密码')

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = User.objects.get(id=self.user.get('id'))
        if not user.check_password(old_password):
            raise forms.ValidationError('旧密码错误')
        return old_password


    def clean_old_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('两次密码不一致')
        return password2

