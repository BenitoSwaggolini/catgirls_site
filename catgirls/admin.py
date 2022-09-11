from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
@admin.register(CatGirl)
class CatGirlAdmin(admin.ModelAdmin):
    list_display = ['initials', 'age', 'height', 'weight', 'virginity', 'photo', 'rank', 'status'] # отображаемые параметры
    list_editable = ['age', 'height', 'weight', 'virginity', 'photo', 'rank', 'status'] # редактируемые параметры
    ordering = ['age', '-virginity']# сортировка по параметрам
    fields = ['initials', 'age', 'height', 'weight', 'virginity', 'photo', 'rank',  'status'] # обязательные поля при создании объекта
    list_filter = ['age', 'rank', 'virginity'] # фильтры по параметрам




@admin.register(CatGirlStatus)
class CatGirlStatusAdmin(admin.ModelAdmin):
    list_display = ['status']
    fields = ['status']

#SenatorArmstrong - name
#SenatorArmstrong - password
#SenatorArmstrong@mail.ru























   # def get_image(self, obj):
   #     return mark_safe(f'<img src={obj.photo.url} width="100" height="60')
   # get_image.short_description = "Фотография"









#SenatorArmstrong - name
#SenatorArmstrong - password
#SenatorArmstrong@mail.ru