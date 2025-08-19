from rest_framework import serializers

from resident.models import House


class HouseSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    class Meta:
        model = House
        fields = ['house_number','address','user']
    # house_number = serializers.IntegerField()
    # address = serializers.CharField(max_length=255)
    # user = serializers.IntegerField()
