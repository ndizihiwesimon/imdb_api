from django.urls import include, path

from rest_framework.routers import DefaultRouter

from watchlist.api.views import WatchList, ReviewCreate, ReviewDetails, ReviewList, StreamPlatformVS, UserReview, WatchListAV, WatchDetailsAV

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='stream-platform')

urlpatterns = [
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream-details'),

    path('', include(router.urls)),

    path('list/', WatchListAV.as_view(), name='Watch-list'),
    path('<int:pk>/', WatchDetailsAV.as_view(), name='WatchList-details'),
    path('new-list/', WatchList.as_view(), name='WatchList-list2'),
    path('<int:pk>/review-create/',
         ReviewCreate.as_view(), name="review-create"),
    path('<int:pk>/reviews/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetails.as_view(), name="review-details"),

    path('user-review/', UserReview.as_view(), name="user-review-details"),
]
