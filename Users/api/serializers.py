from django.contrib.contenttypes.models import ContentType

from Users.models import user

from rest_framework import serializers


class UserInformationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField(allow_blank=True)
    first_name = serializers.CharField(allow_blank=True)
    last_name = serializers.CharField(allow_blank=True)
    phone_number = serializers.CharField(max_length=15, allow_blank=True)
    address = serializers.CharField(min_length=15, max_length=200, allow_blank=True)
    postal_code = serializers.CharField(min_length=9, allow_blank=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'password', 'phone_number', 'address', 'postal_code',
            'img')

class CreditSerializer(serializers.Serializer):
    Amount = serializers.IntegerField()

class MessageSerializer(serializers.Serializer):
    Text = serializers.CharField(max_length = 100)

