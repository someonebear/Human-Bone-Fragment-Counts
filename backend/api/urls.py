from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('elements/', views.ElementList.as_view()),
    path('elements/<str:name__iexact>/', views.ElementDetail.as_view()),
    path('entries/', views.EntryList.as_view()),
    path('entries/<int:pk>/', views.EntryDetail.as_view()),
    path('entry-groups/', views.EntryGroupList.as_view()),
    path('entry-groups/<int:pk>/', views.EntryGroupDetail.as_view()),
    path('landmarks/', views.LandmarkList.as_view()),
    path('landmarks/<str:id__iexact>/', views.LandmarkDetail.as_view()),
    # path('calc/', views.MNICalculation.as_view()),
]

# Example usage - http http://127.0.0.1:8000/api/elements/ Accept:text/html
# Example usage - http http://127.0.0.1:8000/api/elements.json
# http POST http://127.0.0.1:8000/entries/ "Authorization: Token f2144eb3b28f79a5455621c4179336e3b07fa7cc" < api/test_entry.json --offline
urlpatterns = format_suffix_patterns(urlpatterns)
