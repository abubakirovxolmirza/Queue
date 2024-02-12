from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Queue
from .serializers import QueueSerializer

@api_view(['POST'])
def add_queue(request):
    direction = request.data.get('direction')

    latest_queue = Queue.objects.filter(direction=direction).order_by('-queue_number').first()
    queue_number = 1 if not latest_queue else latest_queue.queue_number + 1

    queue = Queue.objects.create(direction=direction, queue_number=queue_number)
    queue.time_received = timezone.now().strftime("%Y.%m.%d %H:%M")
    serializer = QueueSerializer(queue)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_queues(request):
    queues = Queue.objects.all()
    queues_by_direction = {}

    for queue in queues:
        direction = queue.direction
        if direction not in queues_by_direction:
            queues_by_direction[direction] = []
        queues_by_direction[direction].append(queue)

    serialized_queues_by_direction = {}
    for direction, queues in queues_by_direction.items():
        serialized_queues_by_direction[direction] = QueueSerializer(queues, many=True).data

    return Response(serialized_queues_by_direction)


@api_view(['GET'])
def get_queues(request, service_type):
    queues = Queue.objects.filter(direction=service_type)
    serialized_queues = QueueSerializer(queues, many=True).data
    return Response(serialized_queues)


@api_view(['DELETE'])
def delete_queue(request, service_type, queue_number):
    try:
        queue = Queue.objects.get(direction=service_type, queue_number=queue_number)
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.data.get('message') == 'end':
        queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.data.get('message') == 'continue':
        return Response({"detail": "Queue deletion not requested."})
    else:
        return Response({"detail": "Invalid message format."}, status=status.HTTP_400_BAD_REQUEST)
