from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_and_create_project, name='get_all_and_create_project'),
    path('<int:id>/', views.get_project_by_id, name='get_project_by_id'),
    path('update/<int:id>/', views.update_project, name='update_project'),
]
