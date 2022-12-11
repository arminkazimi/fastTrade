from rest_framework import serializers
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'phone_number',
            'email',
            'password',
            'confirm_password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = CustomUser(
            phone_number=self.validated_data['phone_number'],
            email=self.validated_data['email'],
            username=self.validated_data['email'],
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save()
        return user


class MyAuthSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'phone',
            'email'
        ]

    def get_phone(self, obj):
        return str(obj.phone_number)
# {
#             "phone_number": "+989393184940",
#             "email":"ari@gmail.com",
#             "password":"1234",
#             "confirm_password":"1234"
#         }