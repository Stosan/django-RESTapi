from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
import django.utils.timezone

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class PayloadGroup(models.Model):

    id = models.IntegerField(primary_key=True, default=0, editable=False)
    name = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class PayloadDevice(models.Model):
   #device_id = models.ForeignKey(PayloadGroup, on_delete=models.CASCADE)
   device = models.CharField(max_length=20,null=True)
   time = models.CharField(max_length=100, null=True)
   data = models.CharField(max_length=100, null=True)
   seqNumber = models.CharField(max_length=100, null=True)
   deviceTypeId = models.CharField(max_length=100, null=True)
   added_on = models.DateTimeField(auto_now_add=True)
   
   class Meta:
       ordering = ['added_on']
       verbose_name = "deviceTypeId"
       verbose_name_plural = "deviceTypeIds"
   
   def __str__(self):
        return f"{self.device} - {self.time} - {self.data} - {self.seqNumber} - {self.deviceTypeId}"

