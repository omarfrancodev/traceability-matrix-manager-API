from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView, ProjectUsersView

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list'),
    path('<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('<int:pk>/users/', ProjectUsersView.as_view(), name='project-users'),
]
