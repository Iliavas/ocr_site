from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view()),
    path('get_image', CreatePostView.as_view(), name='get_image'),
    path('succes', Succes, name='succes')
]