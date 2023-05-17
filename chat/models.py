from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_chat')
    message = models.CharField(max_length=150)
    create_date = models.DateTimeField()

    class Meta:
        db_table = 'message'
    
    def __str__(self):
        return self.id