from django.db import models


class ModelLog(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    log_version = models.CharField(max_length=200, default='', blank=True)
    file_log = models.FileField(upload_to='log')

    def __str__(self):
        return f'{self.time_create}, {self.log_version}'
