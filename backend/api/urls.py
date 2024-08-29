from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('elements/', views.element_list),
    path('elements/<str:name>/', views.element_detail),
]

# Example usage - http http://127.0.0.1:8000/api/elements/ Accept:text/html
# Example usage - http http://127.0.0.1:8000/api/elements.json
urlpatterns = format_suffix_patterns(urlpatterns)