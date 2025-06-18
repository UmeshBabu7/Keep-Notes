from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home_page, name='home_page'),
    path('search/', views.search_notes, name='search'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='loggedout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
