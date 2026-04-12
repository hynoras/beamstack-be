from rest_framework import serializers


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=225)
    location = serializers.CharField(max_length=200)
    status = serializers.CharField(max_length=2)
    created_at = serializers.DateTimeField(read_only=True)

class UpdateProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=225, required=False)
    location = serializers.CharField(max_length=200, required=False)
    status = serializers.CharField(max_length=2, required=False)
    created_at = serializers.DateTimeField(read_only=True)