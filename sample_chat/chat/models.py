from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)


class Message(models.Model):
    name = models.ForeignKey(Room, related_name="messages")
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)



