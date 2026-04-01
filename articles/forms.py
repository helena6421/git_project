from django import forms
from .models import Article
# 6 лаба
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# 5 лаба
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']

    def clean_title(self):
        title = self.cleaned_data['title']

        if Article.objects.filter(title=title).exists():
            raise forms.ValidationError('Статья с таким названием уже существует')

        return title

# 6 лаба
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError('Пароли не совпадают')

        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)