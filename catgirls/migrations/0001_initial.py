# Generated by Django 4.0.6 on 2022-09-09 12:04

import autoslug.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CatGirlStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CatGirl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=100, unique=True, verbose_name='Инициалы')),
                ('link', autoslug.fields.AutoSlugField(editable=False, populate_from='initials')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(7), django.core.validators.MaxValueValidator(85)], verbose_name='Возраст')),
                ('height', models.IntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(200)], verbose_name='Рост')),
                ('weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(80)], verbose_name='Вес')),
                ('virginity', models.CharField(choices=[('T', 'True'), ('F', 'False')], max_length=10, verbose_name='Чистота')),
                ('photo', models.ImageField(blank=True, null=True, unique=True, upload_to='photos/', verbose_name='Внешний вид')),
                ('price', models.IntegerField(default=10000, verbose_name='Цена')),
                ('rank', models.CharField(choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=50, verbose_name='Ранг')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='get_info', to='catgirls.catgirlstatus', verbose_name='Возрастной статус')),
            ],
            options={
                'ordering': ['age', '-price'],
            },
        ),
    ]
