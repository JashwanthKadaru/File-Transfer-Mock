from rest_framework import serializers
from .models import File, TransferHistory
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FileSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    original_owner = UserSerializer(read_only=True)

    class Meta:
        model = File
        fields = ['id', 'name', 'file', 'owner', 'original_owner', 'created_at']

class TransferHistorySerializer(serializers.ModelSerializer):
    file = FileSerializer(read_only=True)
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = TransferHistory
        fields = ['id', 'file', 'from_user', 'to_user', 'action', 'timestamp']
