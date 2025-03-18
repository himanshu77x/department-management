from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='True')  # Soft delete indicator

    def __str__(self):
        return self.dept_name
