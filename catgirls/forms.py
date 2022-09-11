from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *
from django.core.validators import MinValueValidator, MaxValueValidator


class AddCatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rank'].empty_label = 'Редкость не выбрана'
        self.fields['virginity'].empty_label = 'Статус не указан'

    def clean_initials(self):
        initials = self.cleaned_data['initials']
        if len(initials) > 100:
            raise ValidationError('Длина инициалов превышает 100 символов')
        return initials

    class Meta:
        model = CatGirl
        fields = ['initials',  'age', 'height', 'weight', 'virginity', 'rank', 'price', 'photo', 'status']


class RegisterUserForm(UserCreationForm):
    captcha = CaptchaField()
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(kwargs)
    captcha = CaptchaField()
    name = forms.CharField(label='Имя', max_length=50)
    email = forms.EmailField(label='Почтовый ящик', max_length=80)
    context = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

# class AddCatForm(forms.Form):
#    virgin_status = [('T', 'True'), ('F', 'False')]
#    person_rank = [('S', 'S'), ('A', "A"), ('B', "B"), ('C', "C"), ("D", "D"), ("F", "F")]
#    initials = forms.CharField(max_length=100, label='Инициалы товара')
#    link = forms.SlugField(max_length=256, label='URL', required=False)
#    age = forms.IntegerField(label='Возраст')
#    height = forms.IntegerField(label='Рост')
#    weight = forms.IntegerField(label=
#                                'Вес')
#    virginity = forms.ChoiceField(label='Девственница', choices=virgin_status)
#    price = forms.IntegerField(label='Цена')
#    rank = forms.ChoiceField(label='Редкость (От F до S)', choices=person_rank)
#
