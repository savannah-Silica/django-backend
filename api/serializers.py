
from rest_framework import serializers
from api.models import  User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = "__all__"
