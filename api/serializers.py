from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models.custom_user import User
from .models.event import Events
import datetime

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "gender",
            "nickname",
            "password",
            "password2"
        )
        extra_kwargs = {
            'gender': {'required': True},
            'nickname': {'required': True}
        }
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            gender=validated_data['gender'],
            nickname=validated_data['nickname']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "gender", "nickname", "username"]


class IdealUserSerializer(serializers.ModelSerializer):
    availability_percentage = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "gender", "nickname", "username", "availability_percentage"]

    def get_availability_percentage(self, obj):
        start_date = self.context['start']
        end_date = self.context['end']
        from_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")               # "%Y-%m-%d %H:%M:%S"
        to_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        events = Events.objects.filter(start_time__gte= from_obj.date(), end_time__lte=to_obj.date(), user=obj)
        
        new = []
        for event in events:
            print(event, event.event_title, event.start_time, event.end_time)
            total_time = event.end_time -  event.start_time
            print("total_time >> ",total_time)
            new.append(total_time)
        
        a = 100 - ((sum(new) * 100) / 10)
        return a