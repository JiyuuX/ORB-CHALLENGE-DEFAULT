from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EventViewSet, UpcomingEventsAPIView, EventsByCategoryAPIView

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upcoming/', UpcomingEventsAPIView.as_view(), name='upcoming-events'),
    path('events/', EventViewSet.as_view({'get': 'list', 'post': 'create'}), name='event-list'),

    path('events/<int:pk>/', EventViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='event-detail'),
    path('events/category/<str:category>/', EventsByCategoryAPIView.as_view(), name='events-by-category'),
]

