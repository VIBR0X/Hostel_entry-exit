from rest_framework import serializers
from .models import Hostel

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
            model = Hostel
            fields = ['id', 'h_num', 'username', 'password']