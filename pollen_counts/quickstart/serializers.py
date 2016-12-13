from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pollen_counts.quickstart.models import PollenCounts


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PollenCountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PollenCounts
        fields = ('datetime', 'birch','alder','willow','poplar_aspen','spruce','total_grass')
