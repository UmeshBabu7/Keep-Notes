from django.urls import path
from . import views
import django.contrib.auth.views as auth_views

app_name="notes"
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    
    path('logout/',auth_views.LogoutView.as_view(template_name='loggedout.html'),name='logout'),
    path('home/',views.home_page,name='home_page'),
    path('update/',views.update,name='update'),
    path('register/',views.register,name='register'),
    path('settings/',views.settings,name='settings'),
]
