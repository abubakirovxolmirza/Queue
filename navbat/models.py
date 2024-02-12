from django.db import models

# Create your models here.


class Queue(models.Model):
    direction = models.CharField(max_length=100)
    queue_number = models.IntegerField()
    time_received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.direction} Queue - {self.queue_number}"
