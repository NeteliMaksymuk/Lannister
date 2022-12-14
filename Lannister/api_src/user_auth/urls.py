from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.home_page, name='home'),
    path('register/', views.register, name='register'),
    path('user_detail', views.user_detail, name='user_detail'),
    # path('login/', views.login, name='login'),

]
