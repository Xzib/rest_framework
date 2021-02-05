from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from rest_framework import viewsets
from .models import Manufacturer
from .serializers import ManufacturerApiSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 

# Create your views here.
# class MfgView(APIView):
#     def get(self, request, format=None):
#         print("inside get")
#         model_name = self.kwargs['models_name']
#         mfg_data = Manufacturer.objects.all()
#         serializer = ManufacturerApiSerializer(mfg_data, many=True, context={'request', request})
#         return Response(serializer.data)



class ManufacturerViewset(viewsets.ModelViewSet):
    queryset =  Manufacturer.objects.all()
    serializer_class = ManufacturerApiSerializer

class ManufacturerDetailView(TemplateView):
    template_name = 'rest_model/add-manufacturer.html'
    
    