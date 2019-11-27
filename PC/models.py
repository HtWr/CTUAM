from django.db import models


class PC(models.Model):
    host_name = models.CharField(max_length=15)
    wks_assets_num = models.CharField(max_length=10)
    user_name = models.CharField(max_length=10, default='NULL')

    def __str__(self):
        return self.host_name

