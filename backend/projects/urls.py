from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.ListCreateProjectView.as_view(), name='project_create_list'),
    path('project/<int:pk>/', views.DetailUpdateDeleteProjectView.as_view(), name='project_detail_delete_update'),
]