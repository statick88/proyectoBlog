from django.urls import path
from .views import HolaMundoView

urlpatterns = [
    path('', HolaMundoView.as_view(), name='hola_mundo'),
]
