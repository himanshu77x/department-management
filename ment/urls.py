from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.department_dashboard, name='department_dashboard'),
    path('edit/<int:pk>/', views.edit_department, name='edit_department'),
    path('delete/<int:pk>/', views.delete_department, name='delete_department'),
]
