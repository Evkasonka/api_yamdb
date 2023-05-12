from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    TitleReviewsViewSet,
    ReviewCommentsViewSet,
)

router_v1 = DefaultRouter()
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    TitleReviewsViewSet,
    basename='title-reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    ReviewCommentsViewSet,
    basename='review-comments'
)

v1_prefix = 'v1/'

urlpatterns = [
    path(v1_prefix, include('djoser.urls')),
    path(v1_prefix, include('djoser.urls.jwt')),
    path(v1_prefix, include(router_v1.urls)),
]
