from django.urls import path, re_path, include
from .views import LoginView, home, LogoutView

app_name = 'User_app'
urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    re_path('logout/', LogoutView.as_view(),name='logout'),
    re_path('home/',home,name='home')
]