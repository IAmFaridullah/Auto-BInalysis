from django.db import models
import uuid


class Chat(models.Model):
    msgid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    message = models.CharField(max_length=200)
    sender = models.ForeignKey(
        'userauthentication.client_details', on_delete=models.SET_NULL, related_name='sender_chats', null=True)
    receiver = models.ForeignKey(
        'userauthentication.client_details', on_delete=models.SET_NULL, related_name='receiver_chats', null=True)
    email = models.CharField(max_length=200, null=True)

    msg_time = models.DateTimeField()

    class Meta:
        db_table = 'chats'
