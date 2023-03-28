from django.db import models
import uuid
from userauthentication.models import client_details
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Admin(models.Model):
    Username = models.CharField(max_length=100, primary_key=True)
    Password = models.CharField(max_length=100)
    Admin_Name = models.CharField(max_length=100)
    Admin_Gender = models.CharField(max_length=6, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
    ])

    class Meta:
        db_table = 'admins'


class Chat(models.Model):
    msgid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    message = models.CharField(max_length=200)
    sender_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name='sender_chats', null=True)
    sender_id = models.CharField(max_length=50, null=True)
    sender = GenericForeignKey('sender_type', 'sender_id')
    reciever_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name='reciever_chats', null=True)
    reciever_id = models.CharField(max_length=50, null=True)
    reciever = GenericForeignKey('reciever_type', 'reciever_id')
    msg_time = models.DateTimeField()

    class Meta:
        db_table = 'chats'
