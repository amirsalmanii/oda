from django.urls import path
from . import views


urlpatterns = [
    path('subscribes/', views.SubsCreateListView.as_view(), name='subs_list_create'),
]