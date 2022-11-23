from django.urls import path
from measurement.views import SensorListCreateView, MeasurementCreateView, SensorChangeView, SensorView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/update/<pk>', SensorChangeView.as_view()),
    path('sensors/<pk>', SensorView.as_view()),
]
