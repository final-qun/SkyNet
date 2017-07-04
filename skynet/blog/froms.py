from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='邮箱', max_length=30,)
    pwd = forms.CharField(label='密码',min_length=8, widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    email = forms.EmailField(label='邮箱',max_length=30)
    name = forms.CharField(label='昵称',max_length=15)
    pwd = forms.CharField(label='密码',min_length=8,widget=forms.PasswordInput)
    pwd2 = forms.CharField(label='重新输入密码',min_length=8,widget=forms.PasswordInput)