from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .utils import *
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import CreateView

from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import CatGirl

all_catgirls = CatGirl.objects.all().order_by('age')
categories = CatGirlStatus.objects.all()

def start(request):
    '''Стартовая страница сайта'''
    return render(request, 'shablons/start_place.html')


def shop_page(request):
    items = CatGirl.objects.all()
    sort_by_rank = {'S': 5, 'A': 4, 'B': 3, 'C': 2, 'D': 1.5, "E": 1, 'F': 0}
    sort_by_status = {'Loli': 3, 'Based': 2, 'Milf': 1}
    sorting = sorted(items, key=lambda x: (sort_by_rank[x.rank], sort_by_status[x.status.status]), reverse=True)
    best_cat = sorting[0] if sorting else None
    if len(sorting) > 1:
        del sorting[0]

    contact_list = sorting
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    '''Базовая страница магазина'''
    return render(request, 'shablons/shop_page.html', {'catgirls': all_catgirls, 'page_obj': page_obj, "categories": categories, 'best_cat': best_cat})


def show_one_catgirl(request, name):
    catgirl = get_object_or_404(CatGirl, link=name)

    return render(request, 'shablons/one_catgirl.html', {'catgirl': catgirl})


@login_required(login_url=reverse_lazy('login'))
def add_catgirl(request):
    form = AddCatForm()
    if request.method == 'POST':
        form = AddCatForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()


            print(form.cleaned_data)
    else:
        form = AddCatForm()
    return render(request, 'shablons/add_item.html', {'title': 'Добавление товара', 'form': form})

@login_required(login_url=reverse_lazy('login'))
def show_user_profile(request):
    username = request.user.username
    date_joined = request.user.date_joined
    publications = request.user.published.all()


    return render(request, 'shablons/user_profile.html', {'username': username, 'date_joined': date_joined, 'publications': publications})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shablons/register.html'
    success_url = reverse_lazy('main_page')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('shop')




class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shablons/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_user_context(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('shop')

def logout_user(request):
    logout(request)
    return redirect('login')



class ContactFormView(DataMixin, CreateView):
    form_class = ContactForm
    template_name = 'shablons/contact.html'
    success_url = reverse_lazy('shop')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('shop')



def show_filtered_catgirls(request, one_category):
    filtered = get_object_or_404(CatGirlStatus, status=one_category).get_info.all()




    paginator = Paginator(filtered, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shablons/shop_page.html', {'catgirls': filtered, 'page_obj': page_obj, 'categories': categories})



