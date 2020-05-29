# 'Register' all views for the app in here
# Import the type of view if not already imported and then then add the URL Pattern

from django.urls import path
from .views import ArtistListView, ArtistDetailView, LabelListView, LabelDetailView, CountryListView, CountryDetailView, GenreListView, GenreDetailView, StyleListView, StyleDetailView, RecordingListView, RecordingDetailView, TrackListView, TrackDetailView, CrateListView, CrateDetailView, VideoListView, VideoDetailView

urlpatterns = [
    path('artist/', ArtistListView.as_view()),
    path('artist/<int:pk>/', ArtistDetailView.as_view()),
    path('labels/', LabelListView.as_view()),
    path('labels/<int:pk>/', LabelDetailView.as_view()),
    path('country/', CountryListView.as_view()),
    path('country/<int:pk>/', CountryDetailView.as_view()),
    path('genre/', GenreListView.as_view()),
    path('genre/<int:pk>/', GenreDetailView.as_view()),
    path('style/', StyleListView.as_view()),
    path('style/<int:pk>/', StyleDetailView.as_view()),
    path('recording/', RecordingListView.as_view()),
    path('recording/<int:pk>/', RecordingDetailView.as_view()),
    path('track/', TrackListView.as_view()),
    path('track/<int:pk>/', TrackDetailView.as_view()),
    path('crate/', CrateListView.as_view()),
    path('crate/<int:pk>/', CrateDetailView.as_view()),
    path('video/', VideoListView.as_view()),
    path('video/<int:pk>/', VideoDetailView.as_view()),
]
