from django.urls import path

from .views import BibleVerseView


urlpatterns = [
    path('bible/', BibleVerseView.as_view(), name='bible'),
]