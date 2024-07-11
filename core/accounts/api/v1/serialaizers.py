from rest_framework import serializers
from accounts.models import User

class RecursionSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email' , 'password']
