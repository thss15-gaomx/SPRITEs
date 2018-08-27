from django.db import models


class Block(models.Model):
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)
    width = models.IntegerField(default=1)
    height = models.IntegerField(default=1)
    color = models.CharField(max_length=64, default="#1b1c1d")

    STATUS_DELETED = -1
    STATUS_CREATED = 0
    STATUS_PUBLISHED = 1


class Text(models.Model):
    block = models.OneToOneField(Block, on_delete=models.CASCADE)
    content = models.TextField()
    font_size = models.CharField(max_length=64, default="16px")
    font_color = models.CharField(max_length=64, default="white")


class Pic(models.Model):
    block = models.OneToOneField(Block, on_delete=models.CASCADE)
    content = models.ImageField(upload_to='img')
    name = models.CharField(max_length=100, default="anonymous")