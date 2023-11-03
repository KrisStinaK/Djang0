from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', SportsmanHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', SportsmanCategory.as_view(), name='category')
]
