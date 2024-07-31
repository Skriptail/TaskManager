from django.db import models
class Task(models.Model):
    title = models.CharField('Title', max_length=50)
    task = models.TextField('Task')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name = 'Tasks'
# Create your models here.
