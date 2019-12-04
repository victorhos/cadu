from rest_framework import generics

from .models import Customer
from .serializers import CustomerCreateSerializer, CustomerSerializer


class CustomerListViews(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()

        area_type = self.request.query_params.get('area_type', None)
        region = self.request.query_params.get('region', None)

        if area_type:
            queryset = queryset.filter(type=area_type)
        if region:
            queryset = queryset.filter(location__region=region)

        return queryset


class CustomerCreateViews(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateSerializer


class CustomerRetrieveUpdateDestroyViews(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateSerializer
    lookup_field = 'pk'
