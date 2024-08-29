from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('elements/', views.ElementList.as_view()),
    path('elements/<str:name__iexact>/', views.ElementDetail.as_view()),
    path('entries/', views.EntryList.as_view()),
    path('entries/<int:pk>/', views.EntryDetail.as_view()),
    path('landmarks/', views.LandmarkList.as_view()),
    path('landmarks/<str:id__iexact>/', views.LandmarkDetail.as_view()),
]

# Example usage - http http://127.0.0.1:8000/api/elements/ Accept:text/html
# Example usage - http http://127.0.0.1:8000/api/elements.json
urlpatterns = format_suffix_patterns(urlpatterns)
