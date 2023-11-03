from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, Http404, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from .utils import *


class SportsmanHome(DataMixin, ListView):
    paginate_by = 3
    model = Sportsman
    template_name = 'sportsman/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Sportsman.objects.filter(is_published=True)


# def index(request):
#     posts = Sportsman.objects.all()
#     context = {'posts': posts,
#                'title': 'Главная страница',
#                'menu': menu,
#                'cat_selected': 0,
#                }
#     return render(request, 'sportsman/index.html', context=context)


def about(request):
    contact_list = Sportsman.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sportsman/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'sportsman/add_page.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))

# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'sportsman/add_page.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return render(request, 'sportsman/contact.html')


# def login(request):
#     return render(request, 'sportsman/login.html')


class ShowPost(DataMixin, DetailView):
    model = Sportsman
    template_name = 'sportsman/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

# def show_post(request, post_slug):
#     post = get_object_or_404(Sportsman, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'sportsman/post.html', context=context)


class SportsmanCategory(DataMixin, ListView):
    model = Sportsman
    template_name = 'sportsman/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Sportsman.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


# def show_category(request, cat_id):
#     posts = Sportsman.objects.filter(cat_id=cat_id)
#
#     # if len(posts) == 0:
#     #     raise Http404()
#
#     context = {'posts': posts,
#                'title': 'Отображение по рубрикам',
#                'menu': menu,
#                'cat_selected': cat_id,
#                }
#     return render(request, 'sportsman/index.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'sportsman/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, objectlist=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'sportsman/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')
