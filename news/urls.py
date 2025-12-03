from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('read-later/', views.read_later_list, name='read_later'),
    path('toggle-read-later/', views.toggle_read_later, name='toggle_read_later'),
    path('fetch-news/', views.fetch_news, name='fetch_news'),
]

