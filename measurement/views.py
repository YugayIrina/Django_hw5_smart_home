# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCr eateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from rest_framework import generics
from measurement.models import Sensor, Measurement
from measurement.serializers1 import MeasurementSerializer, SensorDetailSerializer, SensorListSerializer


class ListCreateSensorView(generics.ListCreateAPIView):
    """Создать датчик. Указываются название и описание датчика."""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class ListSensorsView(generics.ListAPIView):
    """Получить список датчиков. Выдается список с краткой информацией по датчикам:
    ID, название и описание"""
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class RetriveUpdateSensorView(generics.RetrieveUpdateAPIView):
    """Получить информацию по конкретному датчику.
    ID, название, описание и список всех измерений с температурой и временем"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class ListCreateMeasurementView(generics.ListCreateAPIView):
    """Добавить измерение. Указываются ID датчика и температура"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
