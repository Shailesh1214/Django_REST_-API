from rest_framework import serializers
from HRM.models import Users


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        #fields = {'name', 'employee_id'}
        fields = '__all__'