from django.urls import path
from apps.Introduction.views import Presentation

app_name = 'Introduction_app'
urlpatterns = [
    path('', Presentation.as_view(), name='presentation'),
]