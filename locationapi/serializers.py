from locationApp.models import BeatPersonnelOne
from rest_framework import serializers
class BeatPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeatPersonnelOne
        fields = '__all__'