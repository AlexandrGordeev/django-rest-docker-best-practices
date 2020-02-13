from abc import ABC

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.CharField(read_only=True)

    def get_token(self, user: User):
        refresh_token = RefreshToken.for_user(user)
        return str(refresh_token.access_token)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        super()
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            instance.save()

        return instance

    class Meta:
        model = User
        fields = ('id', 'email', 'token', 'created_at', 'password', 'is_active')
