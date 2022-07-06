from django.db import models

class Task(models.Model):
    """Modelo que representa una tarea"""

    title = models.CharField(max_length=250)
    completed_task = models.BooleanField(default=False, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-date_created']

    def __str__(self):
        return self.title