# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import viewSerializer
from .models import viewdata

# create a viewset


class viewClass(viewsets.ModelViewSet):
	# define queryset
	queryset = viewdata.objects.all()

	# specify serializer to be used
	serializer_class = viewSerializer
