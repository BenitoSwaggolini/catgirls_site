from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator

virgin_status = [('T', 'True'), ('F', 'False')]
person_rank = [('S', 'S'), ('A', "A"), ('B', "B"), ('C', "C"), ("D", "D"), ("F", "F")]


class CatGirlStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.status}"





class CatGirl(models.Model):
    initials = models.CharField(max_length=100, verbose_name='Инициалы', unique=True)
    link = AutoSlugField(populate_from='initials')
    age = models.IntegerField(validators=[MinValueValidator(7), MaxValueValidator(85)], verbose_name='Возраст')
    height = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(200)], verbose_name='Рост')
    weight = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(80)], verbose_name='Вес')
    virginity = models.CharField(choices=virgin_status, max_length=10, verbose_name='Чистота')
    photo = models.ImageField(null=True, upload_to="photos/", verbose_name='Внешний вид', unique=True)
    price = models.IntegerField(default=10_000, verbose_name='Цена')
    rank = models.CharField(max_length=50, choices=person_rank, verbose_name='Ранг')
    status = models.ForeignKey(CatGirlStatus, related_name='get_info', on_delete=models.SET_NULL, null=True, verbose_name='Возрастной статус')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Продавец', related_name='published')

    def __str__(self):
        return self.initials

    def return_link(self):
        return reverse('one_cat', args=[self.link])

    class Meta:
        ordering = ['age', '-price']


# python manage.py makemigrations
# python manage.py migrate


