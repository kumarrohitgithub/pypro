from rest_framework import serializers
from .models import *


class actorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ["first_name", "last_name"]