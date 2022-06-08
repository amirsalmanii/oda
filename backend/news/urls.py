from django.urls import path
from . import views


urlpatterns = [
    path('news/', views.ListNewsView.as_view(), name='news_list'),
    path('news/create/', views.CreateNewsView.as_view(), name='create_list'),
    path('news/<int:pk>/', views.DetailDeleteNewstView.as_view(), name='news_detail_delete'),
    path('news/u/<int:pk>/', views.UpdateNewstView.as_view(), name='news_update'),
]