from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import viewSerializer
from .models import viewdata
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import JsonResponse
import json
from .models import Order
from .serializers import OrderSerializer
from rest_framework.decorators import action

class viewClass(viewsets.ModelViewSet):
    # define queryset
    queryset = viewdata.objects.all()
    # specify serializer to be used
    serializer_class = viewSerializer
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        # Use the default create method from ModelViewSet
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        order_data = serializer.data

        # Save order data to a JSON file
        with open('order_data.json', 'w') as json_file:
            json.dump(order_data, json_file, indent=4)

        headers = self.get_success_headers(serializer.data)
        return Response(order_data, status=201, headers=headers)