from core.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_active', 'created', 'placements', 'foster_parents', 'foster_siblings']
        read_only_field = ['is_active', 'created']