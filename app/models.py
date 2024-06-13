# app/models.py

from django.db import models


#simple invoice table created
class Invoice(models.Model):
    emp_id = models.CharField(max_length=100)
    emp_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'invoice'
