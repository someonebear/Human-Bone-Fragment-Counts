from django.urls import path

from . import views

urlpatterns = [
    path('elements/', views.element_list),
    path('elements/<str:name>/', views.element_detail),
]