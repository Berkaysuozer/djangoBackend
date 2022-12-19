from rest_framework import serializers
import random

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}},
            "password2": {"style": {"input_type": "password"}},
        }

    def create(self, validated_data):
        validated_data.pop("password2")
        return User.objects.create_user(**validated_data)