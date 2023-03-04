from rest_framework import serializers
from .models import JobModel, InternshipModel
from .models import RegistrationModel, UserModel, ContactModel


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = '__all__'


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipModel
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'
