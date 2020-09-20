from rest_framework import serializers
from .models import Photo




class PhotoSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField( read_only=True)
    
    
    class Meta:
        model = Photo
        fields = '__all__'
        
