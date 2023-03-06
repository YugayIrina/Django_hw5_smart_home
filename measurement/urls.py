from django.urls import path

from . import views
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', views.ListCreateSensorView.as_view()),
    path('sensors/<pk>/', views.RetriveUpdateSensorView.as_view()),
    path('list/', views.ListSensorsView.as_view()),
    path('measurements/', views.ListCreateMeasurementView.as_view()),
]
