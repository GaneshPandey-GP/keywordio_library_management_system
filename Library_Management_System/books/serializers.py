from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Books, User
# from django.contrib.auth.models import User

from books import models


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    confirm_password  = serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model = User
        fields = ['email','username','password','confirm_password']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({"password":"Password must match."})
        user.set_password(password)
        user.save()
        return user    

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
