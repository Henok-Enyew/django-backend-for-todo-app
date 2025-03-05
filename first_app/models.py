from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    is_done = models.BooleanField(default=False)  

    def __str__(self):
        return self.title
