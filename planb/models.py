from django.db import models


class Page(models.Model):
    header = models.IntegerField(default=0)    # 0 -> null
    sidebar = models.IntegerField(default=0)
    footer = models.IntegerField(default=0)
    section_num = models.IntegerField(default=0)
