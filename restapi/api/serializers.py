from rest_framework import serializers
from api.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    title = serializers.CharField(required=True)
    active = serializers.BooleanField()

    def create(self, validated_data):
       return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance