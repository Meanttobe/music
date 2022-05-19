from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django import forms

# 定义MyUser的数据表单，用于用户注册
class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields +('mobile',)
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder': '用户名'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'txt tabInput', 'placeholder': '密码,4-16位数字/字母/特殊符号(空格除外)'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'txt tabInput', 'placeholder': '重复密码'})
        self.fields['mobile'].widget = forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder':'手机号'})