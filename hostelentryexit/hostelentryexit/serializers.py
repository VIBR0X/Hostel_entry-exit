from rest_framework import serializers
from .models import Hostel
from .models import Database
from .models import users

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
            model = Hostel
            fields = ['id', 'h_num', 'username', 'password']


class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
            model = Database
            fields = ['id', 'rollnum_1', 'rollnum_2', 'name_1', 'name_2', 'in_time', 'out_time']

class usersSerializer(serializers.ModelSerializer):
    class Meta:
            model = users
            fields = ['id', 'name', 'roll_no', 'hostel_no', 'room_no', 'hostelvisited']


