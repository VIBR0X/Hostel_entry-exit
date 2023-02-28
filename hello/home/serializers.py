from rest_framework import serializers
from home.models import users
from drf_extra_fields.fields import Base64ImageField

class usersSerializer(serializers.ModelSerializer):
      image=Base64ImageField()
      class Meta:
    
         model = users
         fields = '__all__'
      def create(self, validated_data):
        image=validated_data.pop('image')
        data=validated_data.pop('data')
        return users.objects.create(data=users,image=image)
        
 
   
        
   





       
   

   