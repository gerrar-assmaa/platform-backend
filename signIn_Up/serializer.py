from rest_framework import  serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name','email','groups')
        extra_kwargs = {
            'password':{'write_only': True},
            'email':{ 'validators': [
                UniqueValidator(queryset= User.objects.all())
            ] 
            }
        }
    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            email= validated_data['email'],
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name'],
            password = validated_data['password']
        )

        
        group = validated_data['groups'][0]
        user.groups.add(group)
        return user
        
# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'