# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import *

# Create a model serializer
class viewSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = viewdata
		fields = ('name', 'description')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
		