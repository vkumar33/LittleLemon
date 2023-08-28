# Create your views here.
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import Menu, Booking, MenuItem
from .serializers import menuSerializer,bookingSerializer

'''
# Create your views here.
class bookingview(APIView):

    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = bookingSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": 'success', "data": serializer.data})
        

class menuview(APIView):

    def get(self, request):
        items = Menu.objects.all()
        serializer = menuSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = menuSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": 'success', "data": serializer.data})


'''

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = menuSerializer(queryset, many=True)
        return Response(serializer.data)

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = menuSerializer(queryset)
        return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = bookingSerializer(queryset, many=True)
        return Response(serializer.data)
    