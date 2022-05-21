from django.urls import path

from watchlist.api.views import ReviewDetails, ReviewList, StreamPlatformAV, StreamPlatformDetailsAV, WatchListAV, WatchDetailsAV

urlpatterns = [
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream-details'),

    path('list/', WatchListAV.as_view(), name='Watch-list'),
    path('<int:pk>/', WatchDetailsAV.as_view(), name='WatchList-details'),

    path('stream/<int:pk>/review/', ReviewList.as_view(), name="review-list"),
    path('stream/review/<int:pk>', ReviewDetails.as_view(), name="review-details")
]
