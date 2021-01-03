from django.db import models
from django.utils import timezone
from django.conf import settings
import datetime
import os
# Create your models here.

class TemporaryFile(models.Model):
    key = models.CharField(max_length = 64)
    data = models.FileField()
    time_created = models.DateTimeField(default = timezone.now)

    @property
    def delete_after_time(self):
        if self.time_created < datetime.datetime.now()-datetime.timedelta(minutes=1):
            self_file = TemporaryFile.objects.get(pk = self.pk)
            data = self.data
            os.remove(os.path.join(MEDIA_ROOT, data))
            os.remove(os.path.join(BASE_DIR, data))
            self_file.delete()
            return True
        else:
            return False
