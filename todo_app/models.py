from django.db import models

# Create your models here.
class Todo(models.Model):
    todo=models.CharField(max_length=20)
    description = models.TextField()
    important = models.BooleanField(default=False)

    def __str__(self):
        return f'[{self.pk}]{self.todo}'

    def get_absolute_url(self):
        return '/todo/'