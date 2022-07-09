from email.quoprimime import quote
from django.shortcuts import render

from rest_framework import generics 
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from .permissions import IsAdminUserOrReadOnly
from .models import Quote 
from .serializers import QuoteSerializer
from .paginations import BigSetPagination

class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('-id')
    serializer_class = QuoteSerializer
    permission_classes =  [IsAdminUserOrReadOnly]
    pagination_class = BigSetPagination

    def perform_create(self,serializer):
        quote_author = self.request.user
        serializer.save(quote_author = quote_author)

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
