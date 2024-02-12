from django.urls import path
from .views import add_queue, list_queues, get_queues, delete_queue

urlpatterns = [
    path('add/', add_queue),
    path('adds', list_queues),
    path('recipient/<str:service_type>/', get_queues),
    path('recipient/<str:service_type>/<int:queue_number>', delete_queue),
]
