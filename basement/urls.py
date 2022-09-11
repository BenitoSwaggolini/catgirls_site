"""basement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from catgirls.views import *
urlpatterns = [
    path('admin/', admin.site.urls, name='adminka'),
    path('register/', cache_page(60)(RegisterUser.as_view()), name='register'),
    path('login/', cache_page(60)(LoginUser.as_view()), name='login'),
    path('', cache_page(60)(start), name='main_page'),
    path('shop/', cache_page(60)(shop_page), name='shop'),
    path('shop/add_cat/', add_catgirl, name='add_cat'),
    path('shop/<slug:name>/', show_one_catgirl, name='one_cat'),
    path('logout/', logout_user, name='logout'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('contact/', ContactFormView.as_view(), name='contact_to_admin'),
    path('captcha/', include('captcha.urls')),
    path('shop/<slug:one_category>', show_filtered_catgirls, name='one_category'),
    path('shop/user/account', show_user_profile, name='user_profile')





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()