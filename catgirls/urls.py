from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', start, name='main_page'),
    path('shop/', shop_page, name='shop'),
    path('shop/<str:name>/', show_one_catgirl, name='one_cat')
    ]