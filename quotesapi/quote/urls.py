
from django.urls import path

from .views import QuoteDetailAPIView, QuoteListCreateAPIView

urlpatterns = [
    path('quotes/', QuoteListCreateAPIView.as_view() ),
    path('quotes/<int:pk>/', QuoteDetailAPIView.as_view() )

]