from rest_framework import serializers
from nightowl.models import Movdata
from django.contrib.auth.models import User


class Nserializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Movdata
        fields = ('name','lat','long','rating','price2','owner')

class UserSerializer(serializers.ModelSerializer):
    nightowl = serializers.PrimaryKeyRelatedField(many=True,queryset=Movdata.objects.all())
    class Meta:
        model = User
        fields = ('id','username','nightowl')
