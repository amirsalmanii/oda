from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.ListCreateUsersView.as_view(), name='user_create_list'),
    path('user/<int:pk>/', views.DetailUpdateDeleteUsersView.as_view(), name='user_detail_delete_update'),
]