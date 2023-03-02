from rest_framework import serializers
from .models import Hostel
from .models import Database
from .models import users
from .models import tempdata

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
            model = Hostel
            fields = ['h_num', 'username', 'password']


class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
            model = Database
            fields = ['rollnum_1', 'rollnum_2', 'name_1', 'name_2', 'in_time', 'out_time']

class tempdataSerializer(serializers.ModelSerializer):
      class Meta:
            model = tempdata
            fields = ['rollnum_1', 'rollnum_2', 'name_1', 'name_2', 'in_time']

class usersSerializer(serializers.ModelSerializer):
    class Meta:
            model = users
            fields = ['name', 'roll_no', 'hostel_no', 'room_no']


