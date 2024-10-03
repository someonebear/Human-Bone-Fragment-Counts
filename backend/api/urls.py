from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('elements/', views.ElementList.as_view()),
    path('elements/<str:name__iexact>/', views.ElementDetail.as_view()),
    path('entries/', views.EntryList.as_view()),
    path('entries/<int:pk>/', views.EntryDetail.as_view()),
    path('entry-meta/', views.EntryMetaList.as_view()),
    path('entry-meta/<int:pk>/', views.EntryMetaDetail.as_view()),
    path('landmarks/', views.LandmarkList.as_view()),
    path('landmarks/<str:landmark_id__iexact>/',
         views.LandmarkDetail.as_view()),
    path('individuals/', views.IndividualList.as_view()),
    path('individuals/<str:ind_code__iexact>/',
         views.IndividualDetail.as_view()),
    path('body-parts/', views.BodyPartList.as_view()),
    path('body-parts/<str:bp_code__iexact>/', views.BodyPartDetail.as_view()),
    path('mni/<int:site_pk>/', views.MNICalculation.as_view()),
    path('mni/<int:site_pk>/sex/', views.MNICalculation.as_view()),
]

# Example usage - http http://127.0.0.1:8000/api/elements/ Accept:text/html
# Example usage - http http://127.0.0.1:8000/api/elements.json
# http POST http://127.0.0.1:8000/entries/ "Authorization: Token f2144eb3b28f79a5455621c4179336e3b07fa7cc" < api/test_entry.json --offline
urlpatterns = format_suffix_patterns(urlpatterns)
