from rest_framework import serializers
from accounts.models import User
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password



class RecursionSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length = 255 , write_only = True)

    class Meta:
        model = User
        fields = ['email' , 'password' , 'password2']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({ "detail": "Passwords do not match."})
    
        try:
             # validate the password and catch the exception
           validate_password(attrs.get('password'))
         
         # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password':list(e.messages)})

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
