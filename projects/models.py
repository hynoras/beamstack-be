from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('PL', 'Planned'),
        ('IP', 'In Progress'),
        ('CM', 'Completed'),
    ]
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PL')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
