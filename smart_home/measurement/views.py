from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorChangeSerializer


class SensorListCreateView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # def get(self, request):
    #     sensors = Sensor.objects.all()
    #     serializer = SensorDetailSerializer(sensors, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = SensorDetailSerializer(sensors, many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementCreateView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # def get(self, request):
    #     sensors = Measurement.objects.all()
    #     serializer = MeasurementSerializer(sensors, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = MeasurementSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorChangeView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
