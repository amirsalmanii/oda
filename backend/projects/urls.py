from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.ListProjectView.as_view(), name='project_list'),
    path('project/create/', views.CreateProjectView.as_view(), name='project_create'),
    path('project/<int:pk>/', views.DetailUpdateDeleteProjectView.as_view(), name='project_detail_delete_update'),
]