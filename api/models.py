from django.db import models

# Create your models here.

class TelegramUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    chat_id = models.CharField(max_length=100, unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
