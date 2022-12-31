from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='home'),
    path('<int:course_id>/', views.detail, name='detail'),
]