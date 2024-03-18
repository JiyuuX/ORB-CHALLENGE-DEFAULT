from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from .models import Event
from .serializers import EventSerializer
from django.utils import timezone



class UpcomingEventsAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        now = timezone.now()
        end_time = now + timedelta(days=1)  # Bir sonraki günün başlangıcı

        # Gelecekteki etkinlikleri filtrele
        upcoming_events = Event.objects.filter(date__range=[now.date(), end_time.date()], time__gte=now.time())

        return upcoming_events

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Eğer queryset boşsa, özel bir mesaj içeren Response nesnesi döndür
        if not queryset:
            message = {"message": "There is no upcoming events within 24hr"}
            return Response(message, status=status.HTTP_204_NO_CONTENT)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class EventsByCategoryAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Event.objects.filter(category=category)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

