from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'org_name', 'org_country',
                  'org_city', 'account_name' 'password')
