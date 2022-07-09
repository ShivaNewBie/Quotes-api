from rest_framework import serializers 

from .models import Quote 


class QuoteSerializer(serializers.ModelSerializer):
    quote_author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Quote
        fields = '__all__'
