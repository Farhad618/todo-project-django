from django.db import models

# Create your models here.
class Tasks(models.Model):
	tsk_id = models.AutoField(primary_key=True, editable=False, blank=False)
	usr_id = models.CharField(max_length=20, editable=False, blank=False, null=True)
	tsk_title = models.CharField(max_length=200, blank=False, null=True)
	tsk_desc = models.TextField(blank=True)
	tsk_priority = models.PositiveIntegerField(default=0)
	created_date = models.DateTimeField(editable=False, blank=False, null=True, auto_now_add=True)
	due_date = models.DateField()
	due_time = models.TimeField(null=True)
	is_completed = models.BooleanField(default=False)
