from django.db import models

class Opportunity(models.Model):
    TYPE_CHOICES = (
        ('job', 'Job'),
        ('scholarship', 'Scholarship'),
        ('event', 'Event'),
    )
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    location = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
