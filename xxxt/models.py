from django.db import models
import uuid
# Create your models here.
class download(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid1,editable=False)
    name = models.CharField(max_length=50,unique=True)
    vendor = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    comment = models.TextField()

    def __str__(self):
        return self.name


class sysdownload(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid1,editable=False)
    download = models.ForeignKey(download,related_name='sysdownload',on_delete=models.CASCADE)
    name = models.CharField(max_length=50,unique=True)
    url = models.URLField()