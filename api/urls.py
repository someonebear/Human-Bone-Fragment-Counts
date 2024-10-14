from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('elements/', views.ElementList.as_view()),
    path('elements/<int:pk>/', views.ElementDetail.as_view()),
    path('entries/', views.EntryList.as_view()),
    path('entries/<int:pk>/', views.EntryDetail.as_view()),
    path('entry-meta/', views.EntryMetaList.as_view()),
    path('entry-meta/<int:pk>/', views.EntryMetaDetail.as_view()),
    path('landmarks/', views.LandmarkList.as_view()),
    path('landmarks/<int:pk>/',
         views.LandmarkDetail.as_view()),
    path('individuals/', views.IndividualList.as_view()),
    path('individuals/<str:ind_code__iexact>/',
         views.IndividualDetail.as_view()),
    path('body-parts/', views.BodyPartList.as_view()),
    path('body-parts/<str:bp_code__iexact>/', views.BodyPartDetail.as_view()),
    path('mni/<int:site_pk>/', views.MNICalculation.as_view()),
    path('mni/<int:site_pk>/sex/', views.MNICalculation.as_view()),
    path('sites/', views.SiteList.as_view()),
    path('sites/<int:pk>/', views.SiteDetail.as_view()),
    path('spits/', views.SpitList.as_view()),
    path('spits/<int:pk>/', views.SpitDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
