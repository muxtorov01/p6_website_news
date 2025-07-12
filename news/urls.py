from django.urls import path
from .views import news_view, news_detail_view

urlpatterns = [
    path('', news_view, name='home'),
    path('news/<int:pk>/', news_detail_view, name='news_detail'),
]
