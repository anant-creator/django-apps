import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class all_courses(models.Model):
    course_name = models.CharField(max_length=200)
    inst_name = models.CharField(max_length=100)
    startsfrom = models.DateTimeField('starts from')
    def __str__(self):
        return self.course_name

    def was_publish_recently(self):
        return self.startsfrom >= timezone.now() - datetime.timedelta(days=1)

class details(models.Model):
    course = models.ForeignKey(all_courses, on_delete=models.CASCADE)
    ct = models.CharField(max_length=500)
    your_choice = models.BooleanField(default=False)
    def __str__(self):
        return str(self.ct)
